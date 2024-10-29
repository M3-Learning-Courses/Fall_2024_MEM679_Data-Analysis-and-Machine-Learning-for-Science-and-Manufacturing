import numpy as np
import panel as pn
from scipy.interpolate import interp1d

pn.extension()

ACCENT = "teal"

WIND_SPEED_STD_DEV = 2.0
WIND_SPEED_MEAN = 8.0

WIND_SPEEDS = np.array([0, 3, 6, 9, 12, 15, 18, 21])  # Wind speed (m/s)
POWER_OUTPUTS = np.array([0, 39, 260, 780, 1300, 1300, 0, 0])  # Power output (MW)

# Extract Data

def get_wind_speed():
    # Replace with your wind speed source
    return round(np.random.normal(WIND_SPEED_MEAN, WIND_SPEED_STD_DEV), 1)

wind_speed = get_wind_speed()

# Transform Data

def get_power_output(wind_speed):
    # Replace with your power output calculation
    power_interpolation = interp1d(
        WIND_SPEEDS, POWER_OUTPUTS, kind="linear", fill_value="extrapolate"
    )
    return np.round(power_interpolation(wind_speed), 1)

power_output = get_power_output(wind_speed)

# View Data

wind_speed_view = pn.indicators.Number(
    name="Wind Speed",
    value=wind_speed,
    format="{value} m/s",
    colors=[(10, ACCENT), (100, "red")],
)
power_output_view = pn.indicators.Number(
    name="Power Output",
    value=power_output,
    format="{value} MW",
    colors=[
        (power_output, ACCENT),
        (max(POWER_OUTPUTS), "red"),
    ],
)
indicators = pn.FlexBox(wind_speed_view, power_output_view)

# Layout and style with template

pn.template.FastListTemplate(
    title="WTG Monitoring Dashboard",
    main=[indicators],
    accent=ACCENT,
    main_layout=None,
    theme="dark",
    theme_toggle=False,
    meta_refresh="2",  # Automatically refresh every 2 seconds
).servable();  # The ; is only needed if used in a notebook