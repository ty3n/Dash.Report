# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    overview,
    pi74hc595_Nick,
    IQxel_JamesH,
    feesMins,
    dmm5500,
    newsReviews,
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server
app.title = "MT Journal"
# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dash-financial-report/pi74hc595_Nick":
        return pi74hc595_Nick.create_layout(app)
    elif pathname == "/dash-financial-report/IQxel_JamesH":
        return IQxel_JamesH.create_layout(app)
    # elif pathname == "/dash-financial-report/fees":
    #     return feesMins.create_layout(app)
    elif pathname == "/dash-financial-report/dmm5500":
        return dmm5500.create_layout(app)
    elif pathname == "/dash-financial-report/news-and-reviews":
        return newsReviews.create_layout(app)
    elif pathname == "/dash-financial-report/full-view":
        return (
            overview.create_layout(app),
            pi74hc595_Nick.create_layout(app),
            IQxel_JamesH.create_layout(app),
            # feesMins.create_layout(app),
            dmm5500.create_layout(app),
            newsReviews.create_layout(app),
        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)
