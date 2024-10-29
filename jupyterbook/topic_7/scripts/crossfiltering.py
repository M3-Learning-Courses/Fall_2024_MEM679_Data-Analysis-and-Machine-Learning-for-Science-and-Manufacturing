import holoviews as hv
import numpy as np
import pandas as pd
import panel as pn
from bokeh.models.formatters import NumeralTickFormatter

pn.extension(sizing_mode="stretch_width")

ACCENT = "teal"

SHORT_NAMES = {
    "Changzhou Railcar Propulsion Engineering Research and Development Center": "Changzhou",
    "Siemens Gamesa Renewable Energy": "Siemens Gamesa",
}


@pn.cache()
def get_data():
    data = pd.read_csv("https://assets.holoviz.org/panel/tutorials/turbines.csv.gz")

    mask = data.t_manu.isin(list(SHORT_NAMES))
    data.loc[mask, "t_manu"] = data.loc[mask, "t_manu"].map(SHORT_NAMES)
    data.t_cap = data.t_cap / 10**6 # Convert capacity to gigawatts for readability
    return data

@pn.cache
def get_plots():
    data = get_data()

    # Define shared dataset
    ds = hv.Dataset(data, ["t_manu", "p_year", "t_cap"], "t_cap")

    # Create plots
    ds_by_year = ds.aggregate("p_year", function=np.sum).sort("p_year")[1995:]
    ds_by_manufacturer = ds.aggregate("t_manu", function=np.sum).sort(
        "t_cap", reverse=True
    ).iloc[:20]
    formatter = NumeralTickFormatter(format="0,0")
    plot_by_year = hv.Bars(
        ds_by_year, ("p_year", "Year"), ("t_cap", "Capacity (GW)")
    ).opts(
        responsive=True,
        min_height=300,
        yformatter=formatter,
        color=ACCENT,
        tools=["hover"],
        active_tools=["box_select"],
    )
    plot_by_manufacturer = hv.Bars(
        ds_by_manufacturer, ("t_manu", "Manufacturer"), ("t_cap", "Capacity (GW)")
    ).opts(
        responsive=True,
        min_height=300,
        xrotation=90,
        yformatter=formatter,
        color=ACCENT,
        tools=["hover"],
        active_tools=["box_select"],
    )

    return (plot_by_year + plot_by_manufacturer).cols(1)

crossfilter_plots = hv.link_selections(get_plots()).opts(shared_axes=False)

pn.template.FastListTemplate(
    title="Windturbine Dashboard with Crossfiltering",
    main=[crossfilter_plots],
    main_layout=None,
    accent=ACCENT,
).servable()