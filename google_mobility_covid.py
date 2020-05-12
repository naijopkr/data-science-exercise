import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

world_3let = pd.read_csv('data/2014_World_GDP')[['COUNTRY', 'CODE']]
world_2let = pd.read_csv('data/Global_Mobility_Report.csv', dtype={
    'sub_region_2': object
})

world = world_2let.merge(
    world_3let,
    how = 'inner',
    left_on = ['country_region'],
    right_on = ['COUNTRY']
)

by_country = world.groupby(
    ['country_region_code', 'country_region', 'CODE']
).mean().reset_index()
print(by_country.head())

data = dict(
    type = 'choropleth',
    locations = by_country['CODE'],
    z = by_country['residential_percent_change_from_baseline'],
    text = by_country['country_region'],
    colorbar = { 'title': 'Residential Change from baseline' },
    colorscale = 'blues'
)

layout = dict(
    title = 'Google Mobility from baseline',
    geo = dict(
        showframe = True,
        projection = { 'type': 'mercator' }
    )
)

choromap = go.Figure(data = [data], layout = layout)

pio.write_html(choromap, 'output/covid_mobility.html', auto_open = True)
