import dash_html_components as html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.Div([
            html.Img(src='/static/images/gl.svg', height="70"),
        ], className="gl-logo"),
        html.Hr(),
        html.H3("Capstone Project", className='center fwb'),
        html.H6("Team June ***, Group **", className='v1-space fwb'),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Prediction", href="/predict", active="exact"),
                dbc.NavLink("About", href="/about", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className='sidebar',
)

