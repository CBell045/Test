import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import time

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=True),
        html.Div(id="loading"),
        html.Div(id="page-content")
    ]
)


@app.callback(
    Output("loading", "children"),
    [Input("url", "pathname")]
)
def update_loading(pathname):
    # Simulating a long loading time
    time.sleep(3)
    return html.Div(className="loader", children=[
        html.Div(className="loader-content", children=[
            html.H1("Loading...")
        ])
    ])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def update_page_content(pathname):
    return html.Div("Your application content goes here...")


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
