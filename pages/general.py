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


# forecast function
# def forecast(ticker='AAPL', start='2000-01-01', end='2020-01-01', lookback=60, forecast=30):
def forecast(ticker='AAPL', period='1mo', lookback=60, forecast=30):
    """
    Inputs:
        ticker: stock ticker
        start: starting date for stock history
        end: ening date for stock history
        lookback: how far model looks back for values?
        forecast: how far into the future to forecast price
    Outputs:
        Dataframe with actual stock prices, and a period after it of predicted stock prices
    """
    # download the data
    # df = yf.download(tickers=[ticker], start=start, end=end)
    df = yf.download(tickers=[ticker], period=period)
    y = df['Close'].fillna(method='ffill')
    y = y.values.reshape(-1, 1)

    # scale the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler = scaler.fit(y)
    y = scaler.transform(y)

    # generate the input and output sequences
    X = []
    Y = []

    for i in range(lookback, len(y) - forecast + 1):
        X.append(y[i - lookback: i])
        Y.append(y[i: i + forecast])

    X = np.array(X)
    Y = np.array(Y)

    # fit the model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(lookback, 1)))
    model.add(LSTM(units=50))
    model.add(Dense(forecast))

    # compile and train model
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(X, Y, batch_size=16, epochs=10, verbose=1)

    # generate the forecasts
    X_ = y[-lookback:]  # last available input sequence
    X_ = X_.reshape(1, lookback, 1)

    Y_ = model.predict(X_).reshape(-1, 1)
    Y_ = scaler.inverse_transform(Y_)

    # organize the results in a data frame
    df_past = df[['Close']].reset_index()
    df_past.rename(columns={'index': 'Date', 'Close': 'Actual'}, inplace=True)
    df_past['Date'] = pd.to_datetime(df_past['Date'])
    df_past['Forecast'] = np.nan
    df_past['Forecast'].iloc[-1] = df_past['Actual'].iloc[-1]

    df_future = pd.DataFrame(columns=['Date', 'Actual', 'Forecast'])
    df_future['Date'] = pd.date_range(start=df_past['Date'].iloc[-1] + pd.Timedelta(days=1), periods=forecast)
    df_future['Forecast'] = Y_.flatten()
    df_future['Forecast'] = df_future['Forecast'] + (df_past.iloc[-1]['Actual'] - df_future.iloc[0]['Forecast'])
    df_future['Actual'] = np.nan

    # print(df_past)
    # print(df_future)

    results = pd.concat([df_past, df_future], ignore_index=True).set_index('Date')

    # print(results)

    # Visualize the data
    # plt.figure(figsize=(16, 8))
    # plt.title('Model')
    # plt.xlabel('Date', fontsize=18)
    # plt.ylabel('Close Price USD ($)', fontsize=18)
    # plt.plot(results['Actual'])
    # plt.plot(results['Forecast'])
    # plt.legend(['Actual', 'Forecast'], loc='lower right')
    # plt.show()

    return results


dash.register_page(__name__, path='/')

ALLOWED_TYPES = (
    "text", "number", "password", "email", "search", "tel", "url", "range", "hidden",
)

# This is the layout, the "html" file of a React project if you are familiar those terms
layout = dbc.Container([
    html.H1("General Stocks Forecaster", className='mb-2', style={'textAlign': 'center'}),
    html.Div(
        'Input values into all the fields below, click the "GO" button, and wait for the graph to display. The higher the forecast range chosen, the longer it will take (up to a 3-4 minutes). You can see if the forecast is still running by looking at the title of the tab (should say "Updating...").',
        style={'margin-top': '20px'}),
    html.Div('Ticker Symbol is the symbol of the stock you\'re trying to forecast.', style={'margin-top': '20px'}),
    html.Div('Price History is how far back in time (relative from today) that you want the graph to show.',
             style={'margin-top': '20px'}),
    html.Div(
        'Lookback Range is how far back in time (relative from today) the forecaster looks to train its ML model. The period selected will be used to estimate the values within the forecast range. VALUE MUST BE LESS THAN "Price History"!',
        style={'margin-top': '20px'}),
    html.Div(
        'Forecast Range is how far into the future the model will forecast values. TRY TO KEEP THIS VALUE LESS THAN "Lookback History". Keep in mind that this forecast is not perfect, and the longer the range, the less accurate the model will be.',
        style={'margin-top': '20px'}),

    # input box for ticker symbol, may add more inputs later (such as forecast range)
    dbc.Row([
        dbc.Col([
            html.Div('Ticker Symbol', style={'margin-top': '20px'}),
            dcc.Input(
                id='ticker',
                type='text',
                placeholder='Input ticker symbol, i.e. GOOG',
                debounce=True,
                size='25',  # box length
                style={'margin-right': '10px'},
            ),
        ],
        ),

        dbc.Col([
            html.Div('Price History', style={'margin-top': '20px'}),
            dcc.Dropdown(
                id='period',
                value='period',
                placeholder='Select a period of history to display',
                clearable=False,
                options=['1 Month', '6 Months', '1 Year', '5 Years', '10 Years'],
                style={'margin-right': '10px'},
            ),
        ],
            style=dict(width='20%')),

        dbc.Col([
            html.Div('Lookback Range', style={'margin-top': '20px'}),
            dcc.Dropdown(
                id='lookback-range',
                value='lookback',
                placeholder='Select a period to lookback',
                clearable=False,
                options=['5 Days', '1 Month', '6 Months', '1 Year', '5 Years'],
                style={'margin-right': '10px'},
            ),
        ],
            style=dict(width='15%')),

        dbc.Col([
            html.Div('Forecast Range', style={'margin-top': '20px'}),
            dcc.Dropdown(
                id='forecast-range',
                value='forecast',
                placeholder='Select a period to forecast',
                clearable=False,
                options=['1 Day', '5 Days', '1 Month', '6 Months', '1 Year'],
                style={'margin-right': '10px'},
            ),
        ],
            style=dict(width='15%')),

        html.Button('GO', id='go-button', n_clicks=0,
                    style={'width': '100px', 'height': '50px', 'margin-right': '10px', 'margin-top': '20px'}, ),

    ], style=dict(display='flex'), ),

    html.Div(id='failure-box', style={'color': 'red', 'margin-top': '20px'}),

    # the line graph
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='line-graph-plotly', figure={})
        ], width=12, md=6),

    ], className='mt-4'),

])


# this connects the items in the layout to the to the function immidiately below (in respective input/output orders)
@callback(
    Output('line-graph-plotly', 'figure'),
    Output('failure-box', 'children'),
    Input('go-button', 'n_clicks'),
    State('ticker', 'value'),
    State('period', 'value'),
    State('lookback-range', 'value'),
    State('forecast-range', 'value'),
    prevent_initial_call=True
)
# This section is for creating interactivity between the components of the layout (aka taking inputs like ticker symbol and inputing them into the forecast function, which then goes into the graph)
def plot_data(go_button, ticker, period_hist, lookback_range, forecast_range):
    # translating period history
    period = ''
    match period_hist:
        case '1 Month':
            period = '1mo'
        case '6 Months':
            period = '6mo'
        case '1 Year':
            period = '1y'
        case '5 Years':
            period = '5y'
        case '10 Years':
            period = '10y'

    # translating lookback range
    lb_range = 0
    match lookback_range:
        case '5 Days':
            lb_range = 5
        case '1 Month':
            lb_range = 30
        case '6 Months':
            lb_range = 180
        case '1 Year':
            lb_range = 365
        case '5 Years':
            lb_range = 1825

    # translating forecast range
    fc_range = 0
    match forecast_range:
        case '1 Day':
            fc_range = 1
        case '5 Days':
            fc_range = 5
        case '1 Month':
            fc_range = 30
        case '6 Months':
            fc_range = 180
        case '1 Year':
            fc_range = 365

    # Build the Plotly figure
    try:
        results = forecast(ticker=ticker, period=period, lookback=lb_range, forecast=fc_range)
        fig_line_plotly = px.line(results, x=results.index, y=results.columns[:]).update_xaxes(tickangle=330)
        return fig_line_plotly, ''
    except Exception:
        dummy = pd.DataFrame(dict(x=[1], y=[1]))
        fig_line_plotly = px.line(dummy, x=dummy.x, y=dummy.y)  # .update_xaxes(tickangle=330)
        return fig_line_plotly, 'Failed to create graph (possible reasons: invalid ticker symbol, forecast range >= lookback range >= price history, missing input values)'
