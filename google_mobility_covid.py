import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

world = pd.read_csv('data/Global_Mobility_Report.csv', dtype={
    'sub_region_2': object
})

by_country = world.groupby(
    ['country_region_code', 'country_region']
).mean().reset_index()
print(by_country.head())

data = dict(
    type = 'choropleth',
    locations = by_country['country_region'],
    locationmode = 'country names',
    z = by_country['residential_percent_change_from_baseline'],
    text = by_country['country_region'],
    colorbar = { 'title': 'Residential Change from baseline' },
    colorscale = 'blues'
)

layout = dict(
    title = 'Google Mobility from baseline',
    geo = dict(
        showframe = True,
        projection = { 'type': 'natural earth' }
    )
)

choromap = go.Figure(data = [data], layout = layout)

pio.write_html(choromap, 'output/covid_mobility.html', auto_open = True)
