import pandas as pd
import vizro.plotly.express as px
from vizro import Vizro
import vizro.models as vm

# Load data
df = pd.read_csv('data/moscow_houses.csv')

# Components
scatter_chart = vm.Graph(
    id="scatter_chart",
    figure=px.scatter(
        df, x="Living area", y="Price", color="Region",
        title="Scatter Plot: Living Area vs Price"
    )
)

histogram_chart = vm.Graph(
    # Unique ID
    id="histogram_chart",
    figure=px.histogram(
        df, x="Number of rooms", color="Region",
        title="Histogram: Number of Rooms"
    )
)

# Controls
region_filter = vm.Filter(
    column="Region",
    selector=vm.Dropdown(
        options=df['Region'].unique().tolist(),
        value=df['Region'].unique().tolist()[0]
    )
)

type_filter = vm.Filter(
    column="Apartment type",
    selector=vm.Dropdown(
        options=df['Apartment type'].unique().tolist(),
        value=df['Apartment type'].unique().tolist()[0]
    )
)

# Page
page = vm.Page(
    title="Moscow Housing Dashboard",
    components=[scatter_chart, histogram_chart],
    controls=[region_filter, type_filter]
)

# Dashboard
dashboard = vm.Dashboard(pages=[page])

# Run
Vizro().build(dashboard).run()

#%%
