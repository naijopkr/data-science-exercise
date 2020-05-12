import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

df = pd.read_csv('data/2012_Election_Data')
df = df.rename(columns = {
    'State Abv': 'Code',
    'Voting-Age Population (VAP)': 'VAP'
})
print(df.info())
print(df[['State', 'VAP', 'Code']].head())

data = dict(
    type = 'choropleth',
    colorscale = 'ylorrd',
    locations = df['Code'],
    z = df['VAP'],
    locationmode = 'USA-states',
    text = df['State'],
    marker = dict(
        line = dict(
            color = 'rgb(255, 255, 255)',
            width = 2
        )
    ),
    colorbar = dict(
        title = 'Voting-Age Population (VAP)'
    )
)

layout = dict(
    title = '2012 US Election VAP',
    geo = dict(
        scope = 'usa',
        showlakes = True,
        lakecolor = 'rgb(85, 173, 240)'
    )
)

choromap = go.Figure(data = [data], layout = layout)

pio.write_html(choromap, 'output/us_election_vap.html', auto_open = True)
