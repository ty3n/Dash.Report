import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_current_prices = pd.read_csv(DATA_PATH.joinpath("df_current_prices.csv"))
df_hist_prices = pd.read_csv(DATA_PATH.joinpath("df_hist_prices.csv"))
df_avg_returns = pd.read_csv(DATA_PATH.joinpath("df_avg_returns.csv"))
df_after_tax = pd.read_csv(DATA_PATH.joinpath("df_after_tax.csv"))
df_recent_returns = pd.read_csv(DATA_PATH.joinpath("df_recent_returns.csv"))
df_graph = pd.read_csv(DATA_PATH.joinpath("df_graph.csv"))
tb2_N = pd.read_csv(DATA_PATH.joinpath("tb2_N.csv"))
hc595 = pd.read_csv(DATA_PATH.joinpath("74hc595.csv"))


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["RPi Pins"],
                                        className="subtitle padded",
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("pi.png"),
                                        className="pi",
                                    ),

                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    # html.Strong(
                                    #     ["Programming"],
                                    #     style={
                                    #         "color": "#515151"
                                    #     },
                                    # ),
                                    # html.P(
                                    #     "74hc595 control through GPIO of pi is available as long as we give correct \
                                    #     script to define GPIO behavior which are corresponding to control pin of 74hc595, \
                                    #     so we just choose three GPIO connect SER, RCLK, SRCLK to done it."
                                    # ),
                                    dcc.Markdown('''
```py
import RPi.GPIO as IO       
IO.setwarnings(False)   
IO.setmode (IO.BCM)       
IO.setup(ser,IO.OUT)      
IO.setup(srclk,IO.OUT)
IO.setup(rclk,IO.OUT) 
for y in range(8):
    IO.output(ser,1)
    IO.output(srclk,1)      
    IO.output(srclk,0)   
    IO.output(ser,0)
IO.output(rclk,1)         
time.sleep(0.1)
IO.output(rclk,0)     
```
''')
                                ],
                                className="six columns middle-aligned",
                                style={"color": "#696969"},
                            ),
                        ],
                        className="row ",
                    ),
                    html.Div(
                        [    
                            html.Div(
                                [
                                    html.Strong(
                                        ["Introduction"],
                                        style={
                                            "color": "#515151"
                                        },
                                    ),
                                    html.P(
                                        "Here's a simple way for 74hc595 understanding of GPIO control by using python. \
                                        Based on script of right-top side as well as connection of each pin under right circuit, \
                                        you will done it."
                                    ),
                                    html.Strong(
                                        ["SER"],
                                        style={
                                            "color": "#515151"
                                        },
                                    ),
                                    html.P(
                                        "Data pin, pull high or low for register bit."
                                    ),
                                    html.Strong(
                                        ["SRCLK"],
                                        style={
                                            "color": "#515151"
                                        },
                                    ),
                                    html.P(
                                        "Make store and shift, pull high to low for implementation"
                                    ),
                                    html.Strong(
                                        ["RCLK"],
                                        style={
                                            "color": "#515151"
                                        },
                                    ),
                                    html.P(
                                        "Parallel output pin, output 8bits register."
                                    ),
                                ],
                                className="six columns middle-aligned",
                                style={"color": "#696969"},
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["74HC595 under LED board"],
                                        className="subtitle padded",
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("74hc595.png"),
                                        className="hc595",
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                    html.Div(
                        [          
                            html.Div(
                                [
                                    html.H6(
                                        [
                                            "Control Steps"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    # html.Strong(
                                    #     ["Steps"],
                                    #     style={
                                    #         "color": "#515151"
                                    #     },
                                    # ),
                                    # html.P(
                                    #     "As GPIO pins of left above picture, we can choose three GPIO pin as RCLK, SER, SRCLK control.\
                                    #     Based on LED board circuit of right above picture, we literally connect all of pins with correct \
                                    #     voltage besides control pin of number 5,6,16. Being a 8bit serial-in, parallel-out, \
                                    #     pin 5 as output contorl, pin 6 as data for pulling high or low, pin 16 for shift register use, \
                                    #     so how can we impenment it through pi control, for instance:"
                                    # ),
                                    html.Strong(
                                        ["Step 1"],
                                        style={
                                            "color": "#515151"
                                        },
                                    ),
                                    html.P(
                                        "Initial register 8bit as 00000000, pull data pin high"
                                    ),
                                    html.Strong(
                                        ["Step 2"],
                                        style={
                                            "color": "#515151"
                                        },
                                    ),
                                    html.P(
                                        "pull register shift pin high to low, make register record first bit date on high."
                                    ),
                                    html.Strong(
                                        ["Step 3"],
                                        style={
                                            "color": "#515151"
                                        },
                                    ),
                                    html.P(
                                        "Clear data pin status, pull data pin high to low. Now register status like 00000001."
                                    ),
                                    html.Strong(
                                        ["Step 4"],
                                        style={
                                            "color": "#515151"
                                        },
                                    ),
                                    html.P(
                                        "we continue loop cycle above 3 steps 8 counts, register would become 11111111."
                                    ),
                                    html.Strong(
                                        ["Step 5"],
                                        style={
                                            "color": "#515151"
                                        },
                                    ),
                                    html.P(
                                        "Parallel output, pull enable pin hight to low."
                                    ),
                                ],
                                className="columns middle-aligned",
                                style={"color": "#696969"},
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 2
                    # html.Div(
                    #     [
                    #         html.Div(
                    #             [
                    #                 html.H6("Performance", className="subtitle padded"),
                    #                 dcc.Graph(
                    #                     id="graph-4",
                    #                     figure={
                    #                         "data": [
                    #                             go.Scatter(
                    #                                 x=df_graph["Date"],
                    #                                 y=df_graph["Calibre Index Fund"],
                    #                                 line={"color": "#97151c"},
                    #                                 mode="lines",
                    #                                 name="Calibre Index Fund",
                    #                             ),
                    #                             go.Scatter(
                    #                                 x=df_graph["Date"],
                    #                                 y=df_graph[
                    #                                     "MSCI EAFE Index Fund (ETF)"
                    #                                 ],
                    #                                 line={"color": "#b5b5b5"},
                    #                                 mode="lines",
                    #                                 name="MSCI EAFE Index Fund (ETF)",
                    #                             ),
                    #                         ],
                    #                         "layout": go.Layout(
                    #                             autosize=True,
                    #                             width=700,
                    #                             height=200,
                    #                             font={"family": "Raleway", "size": 10},
                    #                             margin={
                    #                                 "r": 30,
                    #                                 "t": 30,
                    #                                 "b": 30,
                    #                                 "l": 30,
                    #                             },
                    #                             showlegend=True,
                    #                             titlefont={
                    #                                 "family": "Raleway",
                    #                                 "size": 10,
                    #                             },
                    #                             xaxis={
                    #                                 "autorange": True,
                    #                                 "range": [
                    #                                     "2007-12-31",
                    #                                     "2018-03-06",
                    #                                 ],
                    #                                 "rangeselector": {
                    #                                     "buttons": [
                    #                                         {
                    #                                             "count": 1,
                    #                                             "label": "1Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "count": 3,
                    #                                             "label": "3Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "count": 5,
                    #                                             "label": "5Y",
                    #                                             "step": "year",
                    #                                         },
                    #                                         {
                    #                                             "count": 10,
                    #                                             "label": "10Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "label": "All",
                    #                                             "step": "all",
                    #                                         },
                    #                                     ]
                    #                                 },
                    #                                 "showline": True,
                    #                                 "type": "date",
                    #                                 "zeroline": False,
                    #                             },
                    #                             yaxis={
                    #                                 "autorange": True,
                    #                                 "range": [
                    #                                     18.6880162434,
                    #                                     278.431996757,
                    #                                 ],
                    #                                 "showline": True,
                    #                                 "type": "linear",
                    #                                 "zeroline": False,
                    #                             },
                    #                         ),
                    #                     },
                    #                     config={"displayModeBar": False},
                    #                 ),
                    #             ],
                    #             className="twelve columns",
                    #         )
                    #     ],
                    #     className="row ",
                    # ),
                    # Row 3
                    # html.Div(
                    #     [
                    #         html.Div(
                    #             [
                    #                 html.H6(
                    #                     [
                    #                         "74HC595"
                    #                     ],
                    #                     className="subtitle padded",
                    #                 ),
                    #                 html.Div(
                    #                     [
                    #                         html.Table(
                    #                             make_dash_table(df_avg_returns),
                    #                             className="tiny-header",
                    #                         )
                    #                     ],
                    #                     style={"overflow-x": "auto"},
                    #                 ),
                    #             ],
                    #             className="twelve columns",
                    #         )
                    #     ],
                    #     className="row ",
                    # ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [
                                            "74HC595"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        [
                                            html.Table(
                                                make_dash_table(hc595),
                                                className="tiny-header",
                                            )
                                        ],
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 5
                    # html.Div(
                    #     [
                    #         html.Div(
                    #             [
                    #                 html.H6(
                    #                     ["Recent investment returns"],
                    #                     className="subtitle padded",
                    #                 ),
                    #                 html.Table(
                    #                     make_dash_table(df_recent_returns),
                    #                     className="tiny-header",
                    #                 ),
                    #             ],
                    #             className=" twelve columns",
                    #         )
                    #     ],
                    #     className="row ",
                    # ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )