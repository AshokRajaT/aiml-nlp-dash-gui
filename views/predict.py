import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

alerts = dbc.FormGroup([
    html.Br(),
    dbc.Alert(
        "Incident successfully classified !!!",
        id="alert_ok",
        dismissable=True,
        is_open=False,
    ),

    dbc.Alert(
        "Please provide Incident title and summary",
        id="alert_err",
        color="danger",
        dismissable=True,
        is_open=False,
    ),
])

title_input = dbc.FormGroup(
    [
        dbc.Label("Incident Title", html_for="txt_title"),
        dbc.Input(type="text", id="txt_title",autoComplete='off',
                  placeholder="Enter short description incident.", bs_size="sm"),
    ]
)

summary_input = dbc.FormGroup(
    [
        dbc.Label("Incident Summary", html_for="txt_summary"),
        dbc.Textarea(bs_size="sm", id='txt_summary',
                     placeholder="Enter detailed description about the incident", rows=12),
    ]
)

buttons = dbc.FormGroup([
    dbc.Button("Predict", id='btn_predict', outline=True,
               color="primary", className="mr-2"),
    dbc.Button("Reset", id='btn_reset', outline=True,
               color="secondary", className="mr-1", href='/predict', external_link=True),
])

model_list = dbc.FormGroup(
    [
        dbc.Label("Predict With", html_for="dd_model"),
        dcc.Dropdown(
            id="dd_model",
            options=[
                {"label": "All Models", "value": 0},
                {"label": "BERT", "value": 1},
                {"label": "RoBERTa", "value": 2},
                {"label": "DistilBERT", "value": 3},
                {"label": "Electra", "value": 4},
                {"label": "XLNet", "value": 5},
            ],
            value=1, searchable=False, clearable=False
        ),
    ]
)

content_area = dbc.FormGroup([html.Br(),], id="div_content")

form = dbc.Form([alerts, title_input, summary_input,
                 model_list, buttons, content_area])
