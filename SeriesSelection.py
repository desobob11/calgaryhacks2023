import pandas as pd
import numpy as np
from SeriesFormatter import *

import plotly.express as px
import pandas as pd

from dash import Dash, dcc, html, Input, Output, State
from dash import dash_table

app = Dash(__name__)


class SeriesSelection:
    #app = Dash(__name__)
    def __init__(self):
        self._app = Dash(__name__)
        self._sf = SeriesFormatter()
        self._series = None
        self._regions = None
        self.load_options()

        _series_options = [i for i in self._series.keys()]
        _regions_options = ["%s - %s" % (i, self._regions[i]) for i in self._regions.keys()]
        _selected_series = dcc.Textarea(contentEditable=False, id="selected")

        _text = html.Div(children="Hello", id="testlabel")
        _select_button = html.Button("Add Series", id="select", n_clicks = 0)
        _series_dropdown = dcc.Dropdown(options=_series_options, value="Choose series...", multi=True, id="series")
        _regions_dropdown = dcc.Dropdown(options=_series_options, value="Choose series...", multi=True, id="series")
        #build_view()

        self._app.layout = html.Div(children=[
            dcc.Textarea(contentEditable=False, id="selected"),
            html.Div(children="Hello", id="testlabel"),
            html.Button("Add Series", id="select", n_clicks = 0),
            dcc.Dropdown(options=_series_options, value="Choose series...", multi=True, id="series"),
            dcc.Dropdown(options=_series_options, value="Choose series...", multi=True, id="series")
        ])
        if self._app is not None and hasattr(self, "callbacks"):
            self.callbacks(self._app)


    def build_view(self):


        self._app.layout = html.Div(children=[
            self._text,
            self._series_dropdown,
            self._regions_dropdown,
            self._selected_series,
            self._select_button
       ])


    def callbacks(self, _app):

        @_app.callback(
            Output('select', 'children'),
            Input('select', 'n_clicks')
        )
        def refresh():
            self._app

            return "it worked"
        _app.run_server()




    def load_options(self):
        with open("series_data.json", "r") as file:
            self._series = json.load(file)
        with open("regions_data.json", "r") as file:
            self._regions = json.load(file)


    @property
    def sf(self):
        return self._sf


    #def enable_view(self):
      #  self._app.run_server(port=8001)


def main():
    ss = SeriesSelection()
    sf = SeriesFormatter()
    sf.get_series_id()
#    sf.pull_compile_data()


    ss._sf = sf
    ss.load_options()
    #ss.build_view()
    #ss.enable_view()



if __name__ == "__main__":
    main()