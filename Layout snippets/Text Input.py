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
app.layout = html.Div(children=[
    html.Label('Text Input'),
    dcc.Input(
        placeholder='',
        type='text',
        value=''
    )
])

#App server
if __name__ == '__main__':
    app.run_server(debug=True)