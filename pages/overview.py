import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_fund_facts = pd.read_csv(DATA_PATH.joinpath("df_fund_facts.csv"))
df_price_perf = pd.read_csv(DATA_PATH.joinpath("df_price_perf.csv"))
develop = pd.read_csv(DATA_PATH.joinpath("develop.csv"))
history = pd.read_csv(DATA_PATH.joinpath("history.csv"))


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Journal Summary"),
                                    html.Br([]),
                                    html.P(
                                    "First index journal history is kind of version record in order to any format update, \
                                    next assighnment index taht's associated some departments for cooperation on project. \
                                    The index of projects type was classified and present weekly progress. \
                                    For development, we show fourth index on what's development we are engaged in. \
                                    Last one calendar record events recently. You can definitely press Full View or choose any \
                                    project which you want.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Release History"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(history)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Assighnments",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=[
                                                        "10/7",
                                                        "10/14",
                                                        "10/21",
                                                        "10/28",
                                                        "11/4",
                                                    ],
                                                    y=[
                                                        "1",
                                                        "0",
                                                        "0",
                                                        "0",
                                                        "0",
                                                    ],
                                                    marker={
                                                        "color": "#97151c",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="HW",
                                                ),
                                                go.Bar(
                                                    x=[
                                                        "10/7",
                                                        "10/14",
                                                        "10/21",
                                                        "10/28",
                                                        "11/4",
                                                    ],
                                                    y=[
                                                        "5",
                                                        "0",
                                                        "0",
                                                        "0",
                                                    ],
                                                    marker={
                                                        "color": "#dddddd",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="SW",
                                                ),
                                                go.Bar(
                                                    x=[
                                                        "10/7",
                                                        "10/14",
                                                        "10/21",
                                                        "10/28",
                                                        "11/4",
                                                    ],
                                                    y=[
                                                        "3",
                                                        "0",
                                                        "0",
                                                        "0",
                                                    ],
                                                    marker={
                                                        "color": "#a36464",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="PM",
                                                ),
                                                go.Bar(
                                                    x=[
                                                        "10/7",
                                                        "10/14",
                                                        "10/21",
                                                        "10/28",
                                                        "11/4",
                                                    ],
                                                    y=[
                                                        "4",
                                                        "0",
                                                        "0",
                                                        "0",
                                                    ],
                                                    marker={
                                                        "color": "#a1a1a1",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="GIT",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0228945952895,
                                                    "y": -0.189563896463,
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                },
                                                margin={
                                                    "r": 0,
                                                    "t": 20,
                                                    "b": 10,
                                                    "l": 10,
                                                },
                                                showlegend=True,
                                                title="",
                                                width=330,
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 4.5],
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "category",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [0, 22.9789473684],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Projects",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-2",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=[
                                                        "10/7",
                                                        "10/14",
                                                        "10/21",
                                                        "10/28",
                                                        "11/4",
                                                    ],
                                                    y=[
                                                        "10",
                                                        "2",
                                                        "4",
                                                        "5",
                                                        "2",

                                                    ],
                                                    line={"color": "#97151c"},
                                                    mode="lines",
                                                    name="Docsis",
                                                ),
                                                go.Scatter(
                                                    x=[
                                                        "10/7",
                                                        "10/14",
                                                        "10/21",
                                                        "10/28",
                                                        "11/4",
                                                    ],
                                                    y=[
                                                        "8",
                                                        "3",
                                                        "2",
                                                        "6",
                                                        "4",
                                                    ],
                                                    line={"color": "#4d4749"},
                                                    mode="lines",
                                                    name="WiFi",
                                                ),
                                                go.Scatter(
                                                    x=[
                                                        "10/7",
                                                        "10/14",
                                                        "10/21",
                                                        "10/28",
                                                        "11/4",
                                                    ],
                                                    y=[
                                                        "6",
                                                        "7",
                                                        "8",
                                                        "9",
                                                        "1",
                                                    ],
                                                    line={"color": "#a1a1a1"},
                                                    mode="lines",
                                                    name="Pon",
                                                ),
                                                go.Scatter(
                                                    x=[
                                                        "10/7",
                                                        "10/14",
                                                        "10/21",
                                                        "10/28",
                                                        "11/4",
                                                    ],
                                                    y=[
                                                        "6",
                                                        "2",
                                                        "5",
                                                        "5",
                                                        "5",
                                                    ],
                                                    line={"color": "#ba5f74"},
                                                    mode="lines",
                                                    name="Others",
                                                )
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
                                                title="",
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                width=360,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0277108433735,
                                                    "y": -0.142606516291,
                                                    "orientation": "h",
                                                },
                                                margin={
                                                    "r": 20,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 50,
                                                },
                                                showlegend=True,
                                                xaxis={
                                                    "autorange": True,
                                                    "linecolor": "rgb(0, 0, 0)",
                                                    "linewidth": 1,
                                                    # "range": [2008, 2018],
                                                    "showgrid": False,
                                                    "showline": True,
                                                    "title": "",
                                                    # "type": "linear",
                                                },
                                                yaxis={
                                                    "autorange": False,
                                                    "gridcolor": "rgba(127, 127, 127, 0.2)",
                                                    "mirror": False,
                                                    "nticks": 4,
                                                    "range": [0, 20],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "ticklen": 10,
                                                    "ticks": "outside",
                                                    "title": "",
                                                    # "type": "linear",
                                                    "zeroline": False,
                                                    "zerolinewidth": 4,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Development",
                                        className="subtitle padded",
                                    ),
                                    html.Table(make_dash_table(develop)),
                                ],
                                className="six columns",
                            ),
                            # html.Div(
                            #     [
                            #         html.H6(
                            #             "Risk Potential", className="subtitle padded"
                            #         ),
                            #         html.Img(
                            #             src=app.get_asset_url("risk_reward.png"),
                            #             className="risk-reward",
                            #         ),
                            #     ],
                            #     className="six columns",
                            # ),
                        ],
                        className="row ",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(["Calendar"], className="subtitle padded"),
                                    html.Br([]),
                                    # html.Div(
                                    #     [
                                    #         html.Div(
                                    #             [
                                    #                 html.Div(
                                    #                     [
                                    #                         html.Strong(
                                    #                             ["2019/9/27"],
                                    #                             style={
                                    #                                 "color": "#515151"
                                    #                             },
                                    #                         )
                                    #                     ],
                                    #                     className="three columns right-aligned",
                                    #                 ),
                                    #                 html.Div(
                                    #                     [
                                    #                         html.P(
                                    #                             ["Event : EBBU 0.4.1 Release"],
                                    #                             style={
                                    #                                 "color": "#7a7a7a"
                                    #                             },
                                    #                         )
                                    #                     ],
                                    #                     className="nine columns",
                                    #                 ),
                                    #             ],
                                    #             className="row",
                                    #             style={"background-color": "#f9f9f9"},
                                    #         ),
                                    #     ],
                                    #     className="fees",
                                    # ),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        ["2019/09/27"],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        [
                                                            "EBBU 0.4.1 Release"
                                                        ],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "0.4.1 version can be test as usual as we test before since we modified script of raw data format."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    # html.Br([]),
                                                    html.Strong(
                                                        ["EN2251 LED Boart Test"],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "Provide SOP for factory requirement of LED test. Waiting for factory response."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    # html.Br([]),
                                                ],
                                                className="nine columns",
                                            ),
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        ["2019/10/07"],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        [
                                                            "5519 SR3"
                                                        ],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "N/A"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                ],
                                                className="nine columns",
                                            ),
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        ["2019/10/08"],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        [
                                                            "CODA65 SR3"
                                                        ],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "N/A"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                ],
                                                className="nine columns",
                                            ),
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        ["2019/10/07"],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        [
                                                            "CDA-3 FQC Test on GIT"
                                                        ],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "N/A"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                ],
                                                className="nine columns",
                                            ),
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        ["2019/10/21"],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        [
                                                            "DMM5500 Test on GIT"
                                                        ],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "N/A"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                ],
                                                className="nine columns",
                                            ),
                                        ],
                                        className="row",
                                        style={
                                            "background-color": "#f9f9f9",
                                            "padding-bottom": "30px",
                                        },
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )