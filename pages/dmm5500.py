import dash_html_components as html
from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
df_dividend = pd.read_csv(DATA_PATH.joinpath("df_dividend.csv"))
df_realized = pd.read_csv(DATA_PATH.joinpath("df_realized.csv"))
df_unrealized = pd.read_csv(DATA_PATH.joinpath("df_unrealized.csv"))
dmm5500 = pd.read_csv(DATA_PATH.joinpath("dmm5500.csv"))

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 5
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Structure"], className="subtitle padded"
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("dmm5500.png"),
                                        className="DMM5500",
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Br([]),
                                    html.H6(
                                        ["Equipments"],
                                        className="subtitle tiny-header padded",
                                    ),
                                    html.Div(
                                        [
                                            html.Table(
                                                make_dash_table(dmm5500),
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
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Realized/unrealized gains as of 01/31/2018"],
                                        className="subtitle tiny-header padded",
                                    )
                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [html.Table(make_dash_table(df_realized))],
                                className="six columns",
                            ),
                            html.Div(
                                [html.Table(make_dash_table(df_unrealized))],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )