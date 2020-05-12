import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

codes = pd.read_csv('data/2014_World_GDP')[['COUNTRY', 'CODE']]
codes.columns = ['Country', 'Code']
df = pd.read_csv('data/2014_World_Power_Consumption').merge(
    codes,
    how = 'outer',
)
print(df.head())

data = dict(
    type = 'choropleth',
    locations = df['Code'],
    z = df['Power Consumption KWH'],
    text = df['Text'],
    colorbar = dict(
        title = 'Power Consumption KWH'
    )
)

layout = dict(
    title = '2014 World Power Consumption',
    geo = dict(
        showframe = False,
        projection = dict(
            type = 'mercator'
        )
    )
)

choromap = go.Figure(data = [data], layout = layout)

pio.write_html(choromap, 'output/world_power_consumption.html', auto_open = True)
