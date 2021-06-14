from simpletransformers.classification import ClassificationModel, ClassificationArgs
import simpletransformers
from nltk.corpus import stopwords
from dash_bootstrap_components._components.Label import Label
from dash_html_components.Br import Br
from dash_html_components.H3 import H3
from dash_html_components.P import P
from dash_html_components.Span import Span
from future.utils import text_to_native_str
from app import app
import dash.dependencies as dd
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from langdetect import detect
import ftfy
from googletrans import Translator, models
import re
import string
import nltk
import pandas as pd
# nltk.download('words')
nltk.download('stopwords')


def basic_cleanup(dt):
    dt = dt.lower()
    dt = re.sub(r'[\n|\r|\t]', ' ', dt)
    return dt


def remove_email_links(dt):
    dt = re.sub(r'(http|https)://[^\s]*', ' ', dt)
    dt = re.sub(r'\b[^\s]+@[^\s]+[.][^\s]+\b', ' ', dt)
    return dt

def remove_symbols(dt):
  dt = re.sub(r'(http|https)://[^\s]*', ' ', dt)
  dt = re.sub(r'\b[^\s]+@[^\s]+[.][^\s]+\b', ' ', dt)
  dt = re.sub(r'[^\w\s]', ' ', dt)
  dt = re.sub(r'\b\d+\b',' ', dt)
  dt = re.sub(r'\b[a-zA-Z]\b', ' ', dt) 
  dt = re.sub(r'\b[a-zA-Z][a-zA-Z]\b', ' ', dt) 
  dt= ' '.join(dt.split())
  return dt

def custom_stopwords():
    with open("./data/custom_stop_words.txt", 'r', encoding='utf-8') as f:
        dt = f.read()
        return dt.splitlines()

def get_labels():
    with open("./data/labels.txt", 'r', encoding='utf-8') as f:
        dt = f.read().split(',')
        return dt

stopwords = set(stopwords.words('english'))
stopwords = stopwords.union(set(custom_stopwords()))

lables = get_labels()

def render_models(mi, txt):
    mods = {
        0: ['BERT', 'RoBERTa','DistilBERT','Electra', 'XLNet'],
        1: ['BERT'],
        2: ['RoBERTa'],
        3: ['DistilBERT'],
        4: ['Electra'],
        5: ['XLNet']
    }

    mdls = []
    for mod in mods[mi]:
        pth = '/home/ar/work/pys/ply/data/pkls/' + mod.lower() + '/best_model/'
        classifier = ClassificationModel(mod.lower(), pth, use_cuda=False)
        predictions, raw_outputs = classifier.predict([txt])
        ind = lables.index(str(predictions[0]))
        mdl = [
            html.Br(),
            html.Label('Result from ' + mod + ' model is ', className='result_key'), 
            html.Label(' GRP_' + str(predictions[0]), className='result_val'),
            html.Br(),
            html.Label('Score : ' , className='result_key'),
            html.Label(str(raw_outputs[0][ind]), className='result_val'),
            html.Br(),
            html.Br(),
        ]
        print(mod)
        mdls = mdls + mdl
    return mdls


def predict_group(txt_title_value, txt_summary_value, dd_model_value):
    translator = Translator()

    raw_txt = basic_cleanup(txt_title_value + ' ' + txt_summary_value)
    moj_txt = ftfy.fix_text(raw_txt)

    lan_txt = detect(moj_txt)
    eng_txt = moj_txt

    if(lan_txt != 'en'):
        eng_txt = translator.translate(moj_txt, dest='en').text

    lnk_txt = remove_email_links(eng_txt)
    sym_txt = remove_symbols(lnk_txt)
    stp_txt = ' '.join([word for word in sym_txt.split() if word not in stopwords])

    block_1 = html.Div(children=[
        html.Br(),
        html.H1('Prediction Result'),
        html.H3('Text Pre-processing'),
    ])

    table_header = [
        html.Thead(html.Tr([html.Th("Particulars", style={'width': '25%'}), html.Th("Value")]),  className="thead-dark")
    ]

    row1 = html.Tr([html.Td([html.Div("Combined Desc.", className='font-weight-bold'), html.Div("(after converting to lowercase and removing line breaks & tabs)")]), html.Td(raw_txt)])
    row2 = html.Tr([html.Td("Decode Mojibake", className='font-weight-bold'), html.Td(moj_txt)])
    row3 = html.Tr([html.Td("Detected Language", className='font-weight-bold'), html.Td(lan_txt)])
    row4 = html.Tr([html.Td("Translated To English", className='font-weight-bold'), html.Td(eng_txt)])
    row5 = html.Tr([html.Td("Remove Emails and Hyperlinks ", className='font-weight-bold'), html.Td(lnk_txt)])
    row6 = html.Tr([html.Td("Remove Numbers & Symbols ", className='font-weight-bold'), html.Td(sym_txt)])
    row7 = html.Tr([html.Td("Remove Stopwords ", className='font-weight-bold'), html.Td(stp_txt)])

    table_body = [html.Tbody([row1, row2, row3, row4, row5, row6, row7])]

    tbl = dbc.Table(table_header + table_body, bordered=True, hover=True, responsive=True,striped=True)

    block_2 = html.Div(children=[
        html.Br(),
        html.H3('Predicted Group', className='fwb'),
        html.Br()
    ])

    outs = html.Div(children=render_models(dd_model_value, stp_txt))

    return [block_1, tbl, block_2, outs]


@app.callback(
    [
        dd.Output("alert_ok", "is_open"),
        dd.Output("alert_err", "is_open"),
        dd.Output("div_content", "children"),
    ],
    [
        dd.Input("btn_predict", "n_clicks"),
    ],
    [
        dd.State('txt_title', 'value'),
        dd.State('txt_summary', 'value'),
        dd.State('alert_ok', 'is_open'),
        dd.State('alert_err', 'is_open'),
        dd.State('dd_model', 'value')
    ],
)
def output_text(n_clicks, txt_title_value, txt_summary_value, alert_ok_is_open, altert_err_is_open, dd_model_value):
    if dash.callback_context.triggered[0]["prop_id"] == ".":
        return dash.no_update
    else:
        if (txt_title_value is not None and len(txt_title_value) > 0) and (txt_summary_value is not None and len(txt_summary_value) > 0):
            alert_ok_is_open = True
            altert_err_is_open = False
            ctls = predict_group(txt_title_value, txt_summary_value, dd_model_value)
            return [alert_ok_is_open, altert_err_is_open, ctls]
        else:
            alert_ok_is_open = False
            altert_err_is_open = True
            return [alert_ok_is_open, altert_err_is_open, []]
