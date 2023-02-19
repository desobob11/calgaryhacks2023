from dash import *
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

file_items = ["New", "Save", "Export"]
edit_items = ["Copy", "Paste"]
help_items = ["About", "More"]


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
    
def BuildViewBox():
    view_box = html.Div(
        id='view-box', 
        children=[
        html.Div(id="filter-section", children="Filter Settings"), 
        html.Div(id="graph-section", children="Graphs")
    ])
    
    return view_box
    

external_stylesheets = ['./app.css', dbc.themes.BOOTSTRAP]

app = Dash(__name__, external_stylesheets=external_stylesheets)
BuildPage()
app.run_server(debug=True)