import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

df = pd.read_csv('data/2014_World_GDP')

print(df.head())
input()
print(df.columns)
input()

data = dict(
    type = 'choropleth',
    locations = df['CODE'],
    z = df['GDP (BILLIONS)'],
    text = df['COUNTRY'],
    colorbar = { 'title': 'GDP Billions USD'}
)

layout = dict(
    title = '2014 Global GDP',
    geo = dict(
        showframe = False,
        projection = { 'type': 'mercator' }
    )
)

choromap = go.Figure(data = [data], layout = layout)

pio.write_html(choromap, 'output/world_gdp.html', auto_open = True)
