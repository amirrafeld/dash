import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output,State
from dash import Input,Output
from utitlity import create_fig
from utility2 import time_input,time_input1,update_graph
from dash_layout import set_layout
from dash.exceptions import PreventUpdate
import random
x = random.randint(5000,8000)

dash_app = dash.Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])





set_layout(dash_app)

@dash_app.callback(
      Output('timeIntervalButton', 'style'),
     [Input('submitButton', 'n_clicks')])
def temp_time(n_click):
     display = time_input(n_click)
     return display
@dash_app.callback(
        Output('pastDateButtons', 'style'),
        [Input('submitButton', 'n_clicks')])
def temp_time1(n_click):
    dislay = time_input1(n_click)
    return dislay





#
#
@dash_app.callback(
    [Output(component_id='live-graph', component_property='figure')],
    [ Input(component_id='graph-update', component_property='n_intervals'),
        Input(component_id='submitButton', component_property='n_clicks'),
        State(component_id='stockInput', component_property='value'),
        State(component_id='dateButton', component_property='value'),
        State(component_id='timeInterval', component_property='value')],
        prevent_initial_call=True)
def fig(graphUpdate,n_click,stock,date,interval):
    if n_click:
        fig = create_fig(graphUpdate=graphUpdate,n_clicks=n_click,interval=interval,stock_input=stock,period=date)

        #fig.show()
        return [fig]

    else:
        raise PreventUpdate()


@dash_app.callback(Output('graphContainer', 'style'),
                    [Input('submitButton', 'n_clicks')])
def temp_update_graph(n_click):
      display = update_graph(n_click)
      return display


if __name__=='__main__':
    dash_app.run(debug=True,port=x
                 ,dev_tools_hot_reload=False)







# @dash_app.callback(
#     [Output(component_id='live-graph', component_property='figure')],
#     [Input('graph-update', 'n_intervals'),
#      Input(component_id='submitButton', component_property='n_clicks'),
#      Input(component_id='stockInput', component_property='value'),
#      Input(component_id='date', component_property='value')]
#     )
# def temp_create_greaph(interval,n_clicks,stockInput,date):
#     if n_clicks:
#
#         create_fig(n_clicks=n_clicks,stock_input=stockInput,period=date,interval=interval)
#     else:
#         raise PreventUpdate()
from dash import dcc
#
# @dash_app.callback(
#     Output('store-data','data'),
#     [
#          Input(component_id='submitButton', component_property='n_clicks'),
#          State(component_id='stockInput', component_property='value'),
#          State(component_id='dateButton', component_property='value'),
#          State(component_id='timeInterval', component_property='value')],)
# def get_data(n_click,stock_input,date,interval):
#     from utitlity import get_date
#     if n_click:
#
#         df,stock = get_date(n_click=n_click,stock_input=stock_input,period=date,interval=interval)
#         return df.to_dict('stock'),stock
#     else:
#         raise PreventUpdate()
# import pandas as pd
# prevIndex = ''
# @dash_app.callback(
#     Output('graphContainer','children'),
#     Input('store-data','data'))
# def create1(data):
#     from utitlity import create_graph
#     global prevIndex
#     stock = data[1]
#     data = pd.DataFrame(data[0])
#     if (data.index[-1] != prevIndex):
#         prevIndex = data.index[-1]
#         fig  = create_graph(df=data,ticker=stock)
#         return dcc.Graph(figure=fig, animate=True)
#     else:
#         raise PreventUpdate()

