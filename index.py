
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash_html_components.Br import Br
from dash_html_components.Div import Div
from dash_html_components.Spacer import Spacer
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
from app import app,server

import callbacks.cb_predit
import components.common as cc
import components.team_cards as tc
import views.home as home
import views.predict as predict


content = html.Div(id="page-content", children=[], className='content')


app.layout = html.Div([
    dcc.Location(id="url"),
    cc.sidebar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
            html.H1('AIML Capstone - Automatic Ticket Assignment',
                    className='center pb-3'),
            home.home_content,
        ]
    elif pathname == "/predict":
        return [
            html.H1('Predict Group Classification', className='center'),
            predict.form
        ]
    elif pathname == '/about':
        return [
            html.H1('The Team', className='center'),
            tc.tm_cards,
            html.Div([], className='p-3'),
            html.Div([], className='p-3'),
            html.H1('Mentorship & Co-ordination', className='center'),
            html.Div([], className='p-3'),
            tc.sp_cards,
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H1('GUI Tools & Framework', className='center'),
            html.Div([], className='p-3'),
            html.H4('Plotly Dash, VS Code, Git')
        ]

    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not found ..."),
        ], className='mx-auto'
    )


if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
