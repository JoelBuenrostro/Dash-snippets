# -*- coding: utf-8 -*-
#Dash imports
import dash
import dash_core_components as dcc
import dash_html_components as html

#External css style sheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Main app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#App layout, it describes what the applications looks like
app.layout = html.Div([
    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'}
    )
])

#App server
if __name__ == '__main__':
    app.run_server(debug=True)