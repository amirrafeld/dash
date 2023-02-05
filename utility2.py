import time



def update_graph(n_clicks):
    if n_clicks:
        time.sleep(0.95)
        return {'display': 'block'}
    return {'display': 'none'}


def time_input(n):
    if n:
        time.sleep(0.5)
        return {'display': 'block'}
    return {'display': 'none'}


def time_input1(n):
    if n:
        time.sleep(0.5)
        return {'display': 'block'}
    return {'display': 'none'}


def get_date(n_click,stock_input, period, interval):
    if n_click:
        df = yf.download(tickers=stock_input,interval=interval,period=period)
        df['Date'] = df.index

        try:
            return df,stock_input
        except:
            raise PreventUpdate()
    else:
        raise PreventUpdate()




def create_graph(df,ticker,movingAverageNo1='', movingAverageNo2='',
               exponentialMovingAverage='', rsi=False, AverageTrueRange=False, bolinger_band=False,
               plotMacd=False):
   # print(df.columns)



    df = df.set_index('Date')
    print(df)
    if (rsi or AverageTrueRange) and plotMacd:
        spac = [[{"type": "xy", 'secondary_y': True}], [{'type': 'xy', 'secondary_y': True}],
                [{'type': 'xy', 'secondary_y': True}], [{'type': 'xy', 'secondary_y': True}]]
        columns_width = [0.5, 0.2, 0.15, 1, 0.15]
        rowHeights = [0.50, 0.2, 0.15, 0.15]
        rowTitle = [None, None, None, None]
        numberOfRows = 4
        verticalSpacing = 0.07
        columnTitles = [None, None, None, None]
        n = False
    elif (plotMacd == True) and not (rsi or AverageTrueRange):
        spac = [[{"type": "xy", 'secondary_y': True}], [{'type': 'xy', 'secondary_y': True}],
                [{'type': 'xy', 'secondary_y': True}]]
        columns_width = [0.32, 0.43, 0.16]
        rowHeights = [0.50, 0.3, 0.2]
        rowTitle = [None, None, None]
        numberOfRows = 3
        verticalSpacing = 0.02
        columnTitles = [None, None, None]
        n = False

    elif (rsi == True) or (AverageTrueRange == True) or (plotMacd == True):
        columns_width = [0.8, 0.2]
        rowHeights = [0.8, 0.2]
        rowTitle = [None, None]
        numberOfRows = 2
        verticalSpacing = 0.05
        spac = [[{"type": "xy", 'secondary_y': True}], [{'type': 'xy', 'secondary_y': True}]]
        columnTitles = [None, None]
        n = False
    else:
        rowHeights = [1]
        rowTitle = [None]
        numberOfRows = 1
        verticalSpacing = 0
        spac = [[{"type": "xy", 'secondary_y': True}]]
        columnTitles = [None]
        n = True
        columns_width = [1]

    startXline = 34 if plotMacd else 0

    fig = make_subplots(rows=numberOfRows, cols=1, shared_xaxes=True, row_heights=rowHeights, specs=spac,
                        column_titles=columnTitles,
                        row_titles=rowTitle
                        , vertical_spacing=verticalSpacing)

    y0 = df['Adj Close'].min()




    fig.add_trace(go.Ohlc(yaxis='y', xaxis='x',
                                x=df.index,
                                open=df['Open'],
                                high=df['High'],
                                low=df['Low'], opacity=1,
                                close=df['Adj Close'], showlegend=False), row=1, col=1, secondary_y=False)
    fig.add_trace(go.Bar(x=df.index, width=0.66, y=df['Volume'], yaxis='y1', opacity=0.75,
                         orientation='v', xaxis='x',
                         name="Volume", showlegend=False,
                         marker=dict(color='#E0E0E0', line=dict(width=1.2, color='#E0E0E0'), )),
                  secondary_y=True,
                  row=1, col=1),


    fig.update_xaxes(
        tickfont=dict(family='sans-sarif', color='#ffffff', size=14), title_text='Date',
        linewidth=2, linecolor='#ffffff')
    fig.update_xaxes(showgrid=False, zeroline=True,
                     rangebreaks=[dict(bounds=["sat", "mon"]),  # hide weekends, eg. hide sat to before mon
                                  dict(bounds=[16, 9.5], pattern="hour")],
                     tickmode='array')

    fig.update_yaxes(tickfont=dict(family='sans-sarif', color='#ffffff', size=14), title_text='Close', linewidth=2,
                     linecolor='#ffffff')
    fig.update_yaxes(title_text='Volume', row=1, col=1, secondary_y=True)
    fig.update_yaxes(showgrid=False, zeroline=True, secondary_y=True)
    fig.update_yaxes(showgrid=False, zeroline=True, secondary_y=False)

    fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)', 'paper_bgcolor': 'rgba(0,0,0,0)'},
                      title={'text': ticker.upper(), 'font_color': '#ffffff', 'y': 1, 'x': 0.05,
                             'xanchor': 'center', 'yanchor': 'top'},
                      legend_tracegroupgap=4,
                      height=600, width=1000,
                      xaxis_rangeslider_visible=False,
                      yaxis=dict(range=[df['Adj Close'].min(), df['Adj Close'].max()]),
                      xaxis=dict(range=[df.index[0], df.index[-1]]),
                      barmode='group', bargap=0.3,
                      font_family="sans-seri", font_color="#ffffff",

                      title_font_family="sans-seri", title_font_color="#ffffff", font_size=16,
                      legend_title_font_color="#ffffff")
    print('reterun')











    return fig



def layout1(dash1):
    dash1.layout = dbc.Row([
        dbc.Col(
            dbc.RadioItems(
                id="date",
                value='1d',
                className="btn-group btn-group-sm p-0 m-0",

                inputClassName="btn-check p-auto",
                inputStyle={'border': 'border-primary'},
                labelClassName="btn btn-intline-secondary p-auto m-auto",
                labelStyle={'font-size': '11px', 'font-weight': '600', 'margin': '0', 'padding': ' 4px 0px 4px 0px',
                            'width': '50px'},
                labelCheckedClassName="active",
                options=
                [
                    {"label": "1 Day", "value": '1d'},
                    {"label": "5 Days", "value": '5d'},
                    {"label": "6 Month", "value": '6mo'},
                    {"label": "YTD", "value": 'ytd'},
                    {"label": "1 Year", "value": '1y'},
                    {"label": "5 Years", "value": '5y'},
                    {"label": "10 Years", "value": '10y'},
                    {"label": "MAX ", "value": 'max'}
                ]
            ), class_name='col-md-8 col-lg-5', style={'padding': '0'}
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
                value='Borough',
                disabled=False,
                multi=False,
                searchable=True,
                search_value='',
                placeholder='Time Interval',
                clearable=True,
                style={'width': '105px', 'font-size': '11px', 'align-items': 'center',
                       'background-color': 'black', 'font-color': '#ffffff', 'font-weight': '600',
                       },
            ),

        ], class_name='col-md-3 col-lg-2'),

    ])




#
# #  ,class_name='col-2 offset-7',style={'margin-bottom':'18px'},
# dbc.Row([
#                 dbc.Col(
#                     dbc.RadioItems(
#                         id="date",
#                         value='1d',
#                         className="btn-group btn-group-sm p-0 m-0",
#
#                         inputClassName="btn-check p-auto",
#                         inputStyle={'border': 'border-primary'},
#                         labelClassName="btn btn-intline-secondary p-auto m-auto",
#                         labelStyle={'font-size': '11px', 'font-weight': '600', 'margin': '0',
#                                     'padding': ' 4px 0px 4px 0px',
#                                     'width': '50px'},
#                         labelCheckedClassName="active",
#                         options=
#                         [
#                             {"label": "1 Day", "value": '1d'},
#                             {"label": "5 Days", "value": '5d'},
#                             {"label": "6 Month", "value": '6mo'},
#                             {"label": "YTD", "value": 'ytd'},
#                             {"label": "1 Year", "value": '1y'},
#                             {"label": "5 Years", "value": '5y'},
#                             {"label": "10 Years", "value": '10y'},
#                             {"label": "MAX ", "value": 'max'}
#                         ]
#                     ), class_name='col-2', style={'padding': '0'}
#                 ),
#                 dbc.Col([
#                     dcc.Dropdown(
#                         id='timeInterval',
#                         options=[
#                             {'label': '1 Minute', 'value': '1m'},
#                             {'label': '15 Minutes', 'value': '15m"'},
#                             {'label': '30 Minute', 'value': '30m'},
#                             {'label': '60 Minute', 'value': '60m'},
#                             {'label': '1 Day', 'value': '1d'},
#                         ],
#                         optionHeight=15,
#                         value='Borough',
#                         disabled=False,
#                         multi=False,
#                         searchable=True,
#                         search_value='',
#                         placeholder='Time Interval',
#                         clearable=True,
#                         style={'width': '105px', 'font-size': '11px', 'align-items': 'center',
#                                'background-color': 'black', 'font-color': '#ffffff', 'font-weight': '600',
#                                },
#                     ),
#
#                 ], class_name='col-2 ', style={'padding-left': '25px'}),
#
#             ], id='timeContainer', style={'margin-top': '19px', 'display': 'none'}),
