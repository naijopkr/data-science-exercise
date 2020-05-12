import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

from plotly.offline import download_plotlyjs, plot, iplot

data = dict(
    type = 'choropleth',
    locations = ['AZ', 'CA', 'NY'],
    locationmode = 'USA-states',
    colorscale = 'Portland',
    text = ['text1', 'text2', 'text3'],
    z=[1.0, 2.0, 3.0],
    colorbar = { 'title': 'Colorbar title' }
)

layout = dict(geo = { 'scope': 'usa' })

choromap = go.Figure(data = [data], layout = layout)

pio.write_html(choromap, 'output/choromap1.html', auto_open=True)
