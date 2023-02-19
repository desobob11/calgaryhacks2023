import pandas as pd
import numpy as np
from SeriesFormatter import *

import plotly.express as px
import pandas as pd

from dash import Dash, dcc, html, Input, Output, State
from dash import dash_table

app = Dash(__name__)

app.layout = html.Div(children=[

        selected_series = dcc.Textarea(contentEditable=False, id="selected"),

    text = html.Div(children="Hello", id="testlabel")
    select_button = html.Button("Add Series", id="select", n_clicks=0)
    series_dropdown = dcc.Dropdown(options=series_options, value="Choose series...", multi=True,
                                   id="series")
    regions_dropdown = dcc.Dropdown(options=regions_options, value="Choose region...", multi=True,
                                    id="region")
])