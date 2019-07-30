# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        step=0.5,
        value=5,
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)