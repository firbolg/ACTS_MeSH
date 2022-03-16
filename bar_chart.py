import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('MeSH Totals SDoH,Race-Ethnicity,Geography,Disease Type.csv')

mt = df['MeSH term'].tolist()
t = df['MeSH terms'].tolist()

fig = go.Figure(go.Bar(
        x = t, 
        y = mt, 
        orientation='h'
        ))

fig['layout']['yaxis']['autorange'] = "reversed"
fig['layout']['title'] = 'Top 10 MeSH Terms'

fig.update_layout(
                    font_family='Arial',
                    font_color='black',
                    font= dict(size=25),
                    paper_bgcolor='#96c0d9',
                    plot_bgcolor='#dfd3e6'
                    )

fig.show()


