import time
import dash.exceptions
import plotly.tools
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import yfinance as yf
from flask import Blueprint
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.graph_objs as go
from pandas import DataFrame
from plotly.subplots import make_subplots
from pandas_ta import volatility
import ta
from collections import deque
import pandas as pd




def update_dash1(das):
    das.layout = dbc.Container([
        dbc.Row([
            dbc.Col([

                dbc.Label("Ticker", width="auto", className='pe-1'),
                dbc.Col(
                    dbc.Input(id='stockInput', debounce=True, type='text', style={'font-weight': '150px'},
                              placeholder="BTC-USD", valid='BTC-USD'),
                    className="col-5col-lg-3 p-3",
                ),
                dbc.Col(
                    dbc.Button("Submit", id='submitButton', outline=True, color="secondary", className="me-1",
                               style={'margin-top': '14px'}), className='col-2'),

            ], class_name='row row-cols-auto'),

            html.Div([
                dcc.Graph(id='live-graph', animate=True,

                          style={'display': 'none', 'width': '100%'}),
                dcc.Interval(
                    id='graph-update',
                    interval=1000,

                )
            ])

        ]),

        html.Div(id='timeContainer', children=[
            dbc.RadioItems(
                id="date",
                className="btn-group btn-group p-0 m-0",
                inputClassName="btn-check p-auto",
                inputStyle={'border': 'border-primary'},

                labelClassName="btn btn-intline-secondary p-auto m-auto",
                labelStyle={'font-size': '13px', 'font-weight': '500', 'margin': '0', 'padding': '2'},
                labelCheckedClassName="active  ",
                options=[
                    {"label": "1 Day", "value": '1d'},
                    {"label": "5 Days", "value": '5d'},
                    {"label": "6 Month", "value": '6mo'},
                    {"label": "YTD", "value": 'ytd'},
                    {"label": "1 Year", "value": '1y'},
                    {"label": "5 Years", "value": '5y'},
                    {"label": "10 Years", "value": '10y'},
                    {"label": "MAX ", "value": 'max'},

                ],
                value=1,
            ),
        ], className='m-0', style={'display': 'block'},
                 ),

    ], class_name='container-fluid', style={'margin-left': '0px'})
