import dash_bootstrap_components as dbc
from dash import html
from dash import dcc


def set_layout(layout):
    layout.layout = dbc.Container(
        [
            dbc.Row
                (
                [
                    dbc.Col
                        (
                        [
                            dbc.Label("Ticker", )], style={'padding': 'auto', 'margin-top': '8px'},
                        class_name='col-1')
                    ,
                    dbc.Col([dcc.Input(id='stockInput', pattern=r"^[A-Za-z].*", debounce=True, type='text',
                                       style={'font-size': '12px', 'font-color': '#ffffff', 'text-align': 'center',
                                              'font-weight': '150px', 'background-color': 'rgb(6,6,6)',
                                              'border-radius': '20px', 'min-height': '40px', 'padding': "auto"},
                                       placeholder="Enter Symbol")], class_name='col-2 offset-1 col-md-1 offset-md-0',

                            ),
                    dbc.Col(dbc.Button("Submit", id='submitButton', outline=True, color="secondary",
                                       style={'padding': 'auto'},
                                       ), class_name='col-1 offset-2 col-md-1 offset-md-1'),
                ], class_name='mt-3'
            ),
            dbc.Row([
                dbc.Col(
                    dbc.RadioItems(
                        id="dateButton",
                        value='1d',
                        class_name="btn-group btn-group p-auto",
                        input_class_name="btn-check p-auto",
                        labelClassName="btn btn-inline-secondary",
                        labelStyle={'font-size': '9px', 'font-weight': 'bold', 'margin': '0',
                                    'padding': '4px 0px 4px 0px',
                                    'width': '45x'},
                        labelCheckedClassName="active",
                        options=
                        [
                            {"label": "1 Day", "value": '1d'},
                            {"label": "5 Days", "value": '5d'},
                            {"label": "6 Months", "value": '6mo'},
                            {"label": "YTD", "value": 'ytd'},
                            {"label": "1 Year", "value": '1y'},
                            {"label": "5 Years", "value": '5y'},
                            {"label": "10 Years", "value": '10y'},
                            {"label": "MAX ", "value": 'max'}
                        ]
                    ), class_name='col-md-8 col-lg-5', id='pastDateButtons', style={'display': 'none'}
                ),
                dbc.Col([
                    dcc.Dropdown(
                        id='timeInterval',
                        options=[
                            {'label': '1 Minute', 'value': '1m'},
                            {'label': '15 Minutes', 'value': '15m"'},
                            {'label': '30 Minute', 'value': '30m'},
                            {'label': '60 Minute', 'value': '60m'},
                            {'label': '1 Day', 'value': '1d'},
                        ],
                        optionHeight=15,
                        value='1m',
                        disabled=False,
                        multi=False,
                        searchable=True,
                        search_value='',
                        placeholder='Time Interval',
                        clearable=True,
                        style={'width': '90px', 'font-size': '10px', 'align-items': 'center',
                               'background-color': 'rgb(6,6,6)', 'font-color': '#ffffff', 'font-weight': 'bold',
                               },
                    ),

                ], class_name='col-md-2 col-lg-2',id='timeIntervalButton', style={'display': 'none'}),

            ], id='timeContainer', style={"margin-top": '16px'}),

            dbc.Row
                (
                [

                    html.Div
                        (
                        [
                            dcc.Graph(id='live-graph', animate=False,style={'width': '92vw', 'height': '90vh'},config={"displayModeBar": True,
                                            "displaylogo": False,'modeBarButtonsToRemove': ['zoom2d',
                                                'toggleSpikelines','pan2d','select2d','lasso2d','hoverClosestCartesian','hoverCompareCartesian']}),
                            dcc.Interval(id='graph-update',n_intervals=2000)
                        ],id='graphContainer', style={'display': 'none', 'width': '100%','margin-top':'25px','margin-left':'25px'},
                    ),

                ],style=dict(margin='0px')
            ),

        ], class_name='ms-0', fluid=True, style={"margin-top": '25px'})




