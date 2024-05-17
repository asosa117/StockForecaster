# CS 4341, Group 3
# James Cao, Jade McEvoy, Caitlyn Puiia, Andrew Sosa

import dash # pip install dash
from dash import Dash, callback, html, dcc, Input, Output
import plotly.express as px
import dash_ag_grid as dag   # pip install dash-ag-grid
import dash_bootstrap_components as dbc   # pip install dash-bootstrap-components
import pandas as pd   # pip install pandas
pd.options.mode.chained_assignment = None
import matplotlib      # pip install matplotlib
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

# if you get any errors about missing libraries, install them through terminal using: pip install {library name}



app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    html.H1('Stocks Forecaster'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

# this just runs the app
if __name__ == '__main__':
    app.run_server(debug=False, port=8002)
