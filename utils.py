import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    # html.Img(
                    #     src=app.get_asset_url("dash-financial-logo.png"),
                    #     className="logo",
                    # ),
                    html.A(
                        html.Button("Date:2019/10/2", id="learn-more-button"),
                        # href="https://plot.ly/dash/pricing/",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Production Technology Development Division MT Journal")],
                        className="five columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/dash-financial-report/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="seven columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/dash-financial-report/overview",
                className="tab first",
            ),
            dcc.Link(
                "Pi 74HC595 Control",
                href="/dash-financial-report/pi74hc595_Nick",
                className="tab",
            ),
            dcc.Link(
                "IQexl-80 Dual Port Parallel Test",
                href="/dash-financial-report/IQxel_JamesH",
                className="tab",
            ),
            # dcc.Link(
            #     "Fees & Minimums", href="/dash-financial-report/fees", className="tab"
            # ),
            dcc.Link(
                "DMM5500 Test Structure",
                href="/dash-financial-report/dmm5500",
                className="tab",
            ),
            dcc.Link(
                "News & Reviews",
                href="/dash-financial-report/news-and-reviews",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
