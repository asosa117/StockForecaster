# CS 4341, Group 3
# James Cao, Jade McEvoy, Caitlyn Puiia, Andrew Sosa

import dash  # pip install dash
from dash import Dash, callback, html, dcc, Input, Output, State
import plotly.express as px
import dash_ag_grid as dag  # pip install dash-ag-grid
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import pandas as pd  # pip install pandas

pd.options.mode.chained_assignment = None
import matplotlib  # pip install matplotlib

matplotlib.use('agg')
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

import numpy as np
import yfinance as yf
import tensorflow as tf

tf.random.set_seed(0)
from keras.layers import Dense, LSTM
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler

tickerArray = []
priceArray = []

dash.register_page(__name__)

layout = html.Div([
    html.H1("Favorite Stocks", className='mb-2', style={'textAlign': 'center'}),
    dbc.Input(id="input", placeholder="Ticker Symbol", type="text"),
    dbc.Button("Save", id="saveButton", n_clicks=0),
    dbc.Row([
        dbc.Col([
            dbc.FormText("Add favorite ticker and press 'Save' button to save "),
        ], width=4),
    ]),
    html.Br(),
    # Displays the ticker the user input into their favorite stocks
    html.Div(style={'display': 'flex', 'justify-content': 'center', 'background-color': 'gray'}, children=[
        html.Div("Ticker", style={'font-size': '25px'}),
        html.Div("Price($)", style={'paddingLeft': '180px', 'font-size': '25px'}),
    ]),
    dbc.ListGroup(html.Div(id="output", style={'textAlign': 'left', 'font-size': '18px'})),
])

# Sends user input through to grab ticker price when save button clicked
@callback(
    Output("output", "children"),
    [Input("saveButton", "n_clicks")],
    State('input', 'value'),
    prevent_initial_call=True
)
def update_output(n_clicks, value):
    ticker_yahoo = yf.Ticker(value)
    data = ticker_yahoo.history()
    last_quote = data['Close'].iloc[-1]
    # Adds ticker and price values into an array to be displayed above
    if len(value) == 1:
        tickerArray.append(html.Div(style={'display': 'flex', 'justify-content': 'center'},
                                    children=[html.Div(str(value), style={'paddingLeft': '48px'}),
                                              html.Div(str(last_quote), style={'paddingLeft': '225px'})
                                              ]))
    if len(value) == 2:
        tickerArray.append(html.Div(style={'display': 'flex', 'justify-content': 'center'},
                                    children=[html.Div(str(value), style={'paddingLeft': '43px'}),
                                              html.Div(str(last_quote), style={'paddingLeft': '215px'})
                                              ]))
    if len(value) == 3:
        tickerArray.append(html.Div(style={'display': 'flex', 'justify-content': 'center'},
                                    children=[html.Div(str(value), style={'paddingLeft': '52px'}),
                                              html.Div(str(last_quote), style={'paddingLeft': '205px'})
                                              ]))
    if len(value) == 4:
        tickerArray.append(html.Div(style={'display': 'flex', 'justify-content': 'center'},
                                    children=[html.Div(str(value), style={'paddingLeft': '50px'}),
                                              html.Div(str(last_quote), style={'paddingLeft': '190px'})
                                              ]))
    if len(value) > 4:
        tickerArray.append(html.Div(style={'display': 'flex', 'justify-content': 'center'},
                                    children=[html.Div(str(value), style={'paddingLeft': '50px'}),
                                              html.Div(str(last_quote), style={'paddingLeft': '175px'})
                                              ]))
    return tickerArray


