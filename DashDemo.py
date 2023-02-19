import pandas as pd
import numpy as np
from SeriesFormatter import *

import plotly.express as px
import pandas as pd

from dash import Dash, dcc, html, Input, Output, State
from dash import dash_table
from SeriesFormatter import *




sf = SeriesFormatter()
sf.get_series_id()
#    sf.pull_compile_data()

json_format = {}

series = None
regions = None

with open("series_data.json", "r") as file:
    series = json.load(file)
with open("regions_data.json", "r") as file:
    regions = json.load(file)

series_regions_matches = {}


series_options = [i for i in series.keys()]
regions_options = ["%s - %s" % (i, regions[i]) for i in regions.keys()]
#selected_series = dcc.Textarea(contentEditable=False, id="selected")

#text = html.Div(children="Hello", id="testlabel")
#select_button = html.Button("Add Series", id="select", n_clicks=0)
#series_dropdown = dcc.Dropdown(options=series_options, value="Choose series...", multi=True, id="series")
#regions_dropdown = dcc.Dropdown(options=series_options, value="Choose series...", multi=True, id="series")

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(options=regions_options, multi=False, id="regions"),
    dcc.Dropdown(options=series_options, multi=False, id="series"),
    html.Button("Add Series", id="select", n_clicks=0),
    dcc.Textarea(id="testlabel", value="", contentEditable=False),
])


@app.callback(
    Output('testlabel', 'value'),
    Input('select', 'n_clicks'),
    [State('series', 'value'), State('regions', 'value'), State('testlabel', 'value')]
)
def add_item(button, series, region, selected):
    selected_so_far = selected
    next_line = "%s * %s" % (region, series)

    region_code = region.split(" ")[0]

    selected_so_far += next_line
    lines = selected_so_far.split("\n")
    lines = sorted(lines)
    output = ""
    for i in lines:
        output += "%s\n" % i
    if output != "None * None":
        return output



def update_df():




app.run_server(debug=True)


