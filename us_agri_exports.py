import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

df = pd.read_csv('data/2011_US_AGRI_Exports')

print(df['text'].head())

data = dict(
    type = 'choropleth',
    colorscale = 'ylorrd',
    locations = df['code'],
    z = df['total exports'],
    locationmode = 'USA-states',
    text = df['text'],
    marker = dict(line = dict(color = 'rgb(255, 255, 255)', width = 2)),
    colorbar = { 'title': 'Millions USD' }
)

layout = dict(
    title = '2011 US Agriculture Exports by State',
    geo = dict(
        scope='usa',
        showlakes = True,
        lakecolor = 'rgb(85, 173, 240)'
    )
)

choromap = go.Figure(data = [data], layout = layout)

pio.write_html(choromap, 'output/us_agri_exports.html', auto_open = True)
