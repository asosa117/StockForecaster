# CS 4341, Group 3
# James Cao, Jade McEvoy, Caitlyn Puiia, Andrew Sosa

import dash  # pip install dash
import pandas
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
    html.H1("Popular Stocks", className='mb-2', style={'textAlign': 'center'}),
    # Displays the ticker of a list of popular stocks
    html.Div(style={'display': 'flex', 'justify-content': 'center', 'background-color': 'gray', 'font-size': '25px'}, children=[
        html.Div("Ticker", style={'paddingLeft': '50px'}),
        html.Div("Price($)", style={'paddingLeft': '180px'}),
        html.Div("Volume Traded", style={'paddingLeft': '180px'}),
    ]),
    dbc.ListGroup(html.Div(id="popOutput", style={'textAlign': 'left', 'font-size': '18px'})),
    dcc.Interval(
            id='interval_component',
            interval=1*10000, # in milliseconds
            n_intervals=0
        )

])

# Sends output from update function
@callback(
    Output("popOutput", "children"),
    Input("interval_component", "n_intervals")
)
def update_output(n_clicks):
    tickerArray.clear()
    tickers = ["UBER", "LCID", "PFE", "TSLA", "AAPL", "AMZN", "PLTR", "ET", "F", "INTC", "BAC", "MSFT", "PCG", "NIO", "AMD", "T", "KO", "CMCSA", "RIVN", "CSCO", "GOOG", "OPEN", "XOM", "MARA", "SOFI"]
    for value in tickers:
        ticker_yahoo = yf.Ticker(value)
        data = ticker_yahoo.history()
        last_quote = data['Close'].iloc[-1]
        volume = data['Volume'].iloc[-1]
        # Adds ticker and price values into an array to be displayed above
        tickerArray.append(html.Div(style={'display': 'flex', 'justify-content': 'center'},
                                    children=[html.Div(str(value)),
                                              html.Div(str(last_quote), style={'paddingLeft': '180px'}),
                                              html.Div(str(volume), style={'paddingLeft': '180px'}),
                                              ]))
    return tickerArray


