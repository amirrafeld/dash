from dash.exceptions import PreventUpdate
from collections import deque
import plotly.graph_objects as go
import yfinance as yf
from plotly.subplots import make_subplots

dfDeque = deque()

api_key = 'UeUeEoXrSA69rIN1C8VEnCWHOyklxzJI'



def create_fig(graphUpdate,n_clicks, stock_input, period, interval,
               movingAverageNo1=None, movingAverageNo2=None,
               exponentialMovingAverage=None, rsi=False, AverageTrueRange=False, bolinger_band=False,
               plotMacd=False):
    try:


        ticker = stock_input.upper()

        try:
            dfx = yf.download(tickers=ticker, period=period, interval=interval)
            formatTime = ['1m','15m','30m']

            dfx['dateFormat']= dfx.index


            if interval in formatTime:
                dfx['dateFormat'] = dfx['dateFormat'].dt.strftime("%a, %H:%M:%S")

            elif  interval == '60m' or interval == '30m':
                dfx['dateFormat'] = dfx['dateFormat'].dt.strftime("H%/%d/")
            else:
                dfx['dateFormat'] = dfx['dateFormat'].dt.strftime("%d/%m/%y")




            df = dfx.copy()

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

            fig.add_trace(go.Candlestick(yaxis='y', xaxis='x',
                                         x=df['dateFormat'],
                                         open=df['Open'], whiskerwidth=1,
                                         high=df['High'],
                                         low=df['Low'], opacity=1,
                                         close=df['Adj Close'], showlegend=False), row=1, col=1, secondary_y=False)



            fig.add_trace(go.Bar(x=df['dateFormat'], width=0.26, y=df['Volume'], yaxis='y1', opacity=0.35,
                                 orientation='v', xaxis='x',
                                 name="Volume", showlegend=False,
                                 marker=dict(color='#E0E0E0', line=dict(width=1.2, color='#E0E0E0'), )),
                          secondary_y=True,
                          row=1, col=1),


            fig.update_xaxes(
                tickfont=dict(family='sans-sarif', color='#ffffff', size=14),title_text='Date',
                linewidth=2, linecolor='#ffffff')
            fig.update_xaxes(showgrid=False, zeroline=True,rangebreaks=[dict(bounds=["sat", "mon"]),  # hide weekends, eg. hide sat to before mon
              dict(bounds=[16, 9.5], pattern="hour")])

            fig.update_yaxes(tickfont=dict(family='sans-sarif', color='#ffffff', size=14),title_text='Close', linewidth=2, linecolor='#ffffff')
            fig.update_yaxes(title_text='Volume', row=1, col=1, secondary_y=True)
            fig.update_yaxes(showgrid=False, zeroline=True, secondary_y=True)
            fig.update_yaxes(showgrid=False ,zeroline=True,secondary_y=False)


            fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)', 'paper_bgcolor': 'rgba(0,0,0,0)'},
                              title={'text': ticker.upper(), 'font_color': '#ffffff', 'y': 1, 'x': 0.05,
                                     'xanchor': 'center', 'yanchor': 'top'},
                      legend_tracegroupgap=4,

                              xaxis_rangeslider_visible=False,
                              yaxis=dict(range=[df['Adj Close'].min(), df['Adj Close'].max()]),
                              xaxis=dict(range=[df.index[0], df.index[-1]],tickmode='auto',tickangle=45,
                                         tick0=df['dateFormat'][0],tickfont=dict(color='#ffffff',size=8,family='sans-sarif'),nticks=80

            ),
                              barmode='group', bargap=0.2,
                              font_family="sans-seri", font_color="#ffffff",

                              title_font_family="sans-seri", title_font_color="#ffffff", font_size=16,
                              legend_title_font_color="#ffffff")
            print('reterun')
            return fig

        except:
            dfDeque.pop()
            pass
    except:
        raise PreventUpdate


