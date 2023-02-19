from dash import *
import dash_bootstrap_components as dbc
import plotly.express as px
from SeriesFormatter import *

import pandas as pd
import numpy as np
from PullSeries import load_jsons



file_items = ["New", "Save", "Export"]
edit_items = ["Copy", "Paste"]
help_items = ["About", "More"]


load_jsons()

def BuildPage():
    app.layout = html.Div(id='page', children=[
        html.Div(id="page-title",
                 children=[
                     html.H1("WB Dashboard")
                    ]),            
        html.Div(id='navbar',
                 children=[
                     BuildNavbar()
                    ]),
                    BuildViewBox()
    ])
    
def BuildNavbar():
    nav = dbc.Nav(
    [
        BuildDropDownMenu("file-button", "File", file_items),
        BuildDropDownMenu("edit-button", "Edit", edit_items),
        BuildDropDownMenu("help-button", "Help", help_items)
    ])
    return nav

def BuildDropDownMenu(id, label, menu_items):
    #Creates pop up menus for navbar buttons
    
    drop_down_options = []
    for item in menu_items:
        drop_down_options.append(dbc.DropdownMenuItem(item))
    
    drop_down_menu = dbc.DropdownMenu(id=id, label=label, children = drop_down_options, nav=True)
    return drop_down_menu


sf = SeriesFormatter()
sf.get_series_id()
#    sf.pull_compile_data()

json_format = {}

series = None
regions = None

data_dict = {}

with open("series_data.json", "r") as file:
    series = json.load(file)
with open("regions_data.json", "r") as file:
    regions = json.load(file)

series_regions_matches = {}

series_options = [i for i in series.keys()]
regions_options = ["%s - %s" % (i, regions[i]) for i in regions.keys()]
    
def BuildViewBox():
    view_box = html.Div(
        id='view-box', 
        children=[
        html.Div(id="filter-section", 
                 children=[
                     "Filter Settings", 
                    dcc.Dropdown(options=regions_options, multi=False, id="regions"),
                    dcc.Dropdown(options=series_options, multi=False, id="series"),
                    html.Button("Add Series", id="select", n_clicks=0),
                    html.Button("Pull Series", id="pull", n_clicks=0),
                    dcc.Textarea(id="testlabel", value="", contentEditable=False),
                    html.Div(children="", id="pull_proxy")]), 
                    html.Div(id="graph-section", children="Graphs")
    ])
    
    return view_box
    

external_stylesheets = ['./app.css', dbc.themes.BOOTSTRAP]

app = Dash(__name__, external_stylesheets=external_stylesheets)
BuildPage()
@app.callback(
    Output('testlabel', 'value'),
    Input('select', 'n_clicks'),
    [State('series', 'value'), State('regions', 'value'), State('testlabel', 'value')]
)
def add_item(button, series, region, selected):
    selected_so_far = selected
    next_line = "%s * %s" % (region, series)
    if region is not None:
        region_code = region.split(" ")[0]
        update_dictionary(series, region_code)

    selected_so_far += next_line
    lines = selected_so_far.split("\n")
    lines = sorted(lines)
    output = ""
    for i in lines:
        output += "%s\n" % i
    return output


@app.callback(
    Output('pull_proxy', 'children'),
    Input('pull', 'n_clicks')
)
def pull_data(pull):
    try:
        data_dict = sf.pull_compile_data(json_format)
        for i in data_dict:
            data_dict[i].to_csv("%s.csv" % i)
    except:
        pass


def update_dictionary(series_name, region_code):
    try:
        json_format[series_name].append(region_code)
    except KeyError:
        json_format[series_name] = [region_code]


app.run_server(debug=True)