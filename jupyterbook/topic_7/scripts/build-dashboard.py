import hvplot.pandas
import pandas as pd
import panel as pn

pn.extension("tabulator")

ACCENT = "teal"

styles = {
    "box-shadow": "rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px",
    "border-radius": "4px",
    "padding": "10px",
}

# Extract Data

@pn.cache()  # only download data once
def get_data():
    return pd.read_csv("https://assets.holoviz.org/panel/tutorials/turbines.csv.gz")

source_data = get_data()

# Transform Data

min_year = int(source_data["p_year"].min())
max_year = int(source_data["p_year"].max())
top_manufacturers = (
    source_data.groupby("t_manu").p_cap.sum().sort_values().iloc[-10:].index.to_list()
)

def filter_data(t_manu, year):
    data = source_data[(source_data.t_manu == t_manu) & (source_data.p_year <= year)]
    return data

# Filters

t_manu = pn.widgets.Select(
    name="Manufacturer",
    value="Vestas",
    options=sorted(top_manufacturers),
    description="The name of the manufacturer",
)
p_year = pn.widgets.IntSlider(name="Year", value=max_year, start=min_year, end=max_year)

# Transform Data 2

df = pn.rx(filter_data)(t_manu=t_manu, year=p_year)
count = df.rx.len()
total_capacity = df.t_cap.sum()
avg_capacity = df.t_cap.mean()
avg_rotor_diameter = df.t_rd.mean()

# Plot Data

fig = (
    df[["p_year", "t_cap"]].groupby("p_year").sum() / 10**6
).hvplot.bar(
    title="Capacity Change",
    rot=90,
    ylabel="Capacity (GW)",
    xlabel="Year",
    xlim=(min_year, max_year),
    color=ACCENT,
)

# Display Data

image = pn.pane.JPG("https://assets.holoviz.org/panel/tutorials/wind_turbines_sunset.png")

indicators = pn.FlexBox(
    pn.indicators.Number(
        value=count, name="Count", format="{value:,.0f}", styles=styles
    ),
    pn.indicators.Number(
        value=total_capacity / 1e6,
        name="Total Capacity (GW)",
        format="{value:,.1f}",
        styles=styles,
    ),
    pn.indicators.Number(
        value=avg_capacity/1e3,
        name="Avg. Capacity (MW)",
        format="{value:,.1f}",
        styles=styles,
    ),
    pn.indicators.Number(
        value=avg_rotor_diameter,
        name="Avg. Rotor Diameter (m)",
        format="{value:,.1f}",
        styles=styles,
    ),
)

plot = pn.pane.HoloViews(fig, sizing_mode="stretch_both", name="Plot")
table = pn.widgets.Tabulator(df, sizing_mode="stretch_both", name="Table")

# Layout Data

tabs = pn.Tabs(
    plot, table, styles=styles, sizing_mode="stretch_width", height=500, margin=10
)

pn.template.FastListTemplate(
    title="Wind Turbine Dashboard",
    sidebar=[image, t_manu, p_year],
    main=[pn.Column(indicators, tabs, sizing_mode="stretch_both")],
    main_layout=None,
    accent=ACCENT,
).servable()