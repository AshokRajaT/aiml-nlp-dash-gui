import dash_html_components as html
import dash_bootstrap_components as dbc

ar_card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/male.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Ashok Raja T", className="card-title"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

vr_card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/male.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Varchas Doshi", className="card-title"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

pu_card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/male.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Puneet karna", className="card-title"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

mi_card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/female.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Mielu Alex", className="card-title"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

nr_card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/male.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Neeraj Rawat", className="card-title"),
            ]
        ),
    ],
    style={"width": "18rem"},
)


kp_card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/male.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Kapil", className="card-title"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

dv_card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/female.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Divya", className="card-title"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

dm_card = dbc.Card([], style={'backgroundColor': '#F0F0F0', 'border': 'none'})
tm_cards = dbc.CardDeck([vr_card, pu_card, mi_card, nr_card, ar_card, ])
sp_cards = dbc.CardDeck([kp_card, dv_card, dm_card, dm_card, dm_card])
