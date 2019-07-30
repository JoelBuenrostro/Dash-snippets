# -*- coding: utf-8 -*-
#Dash imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#External css style sheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Main app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#App layout, it describes what the applications looks like
app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div')
])

#Callbacks for interactivity
@app.callback(
    Output('my-div', 'children'),
    [Input('my-id', 'value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

#App server
if __name__ == '__main__':
    app.run_server(debug=True)