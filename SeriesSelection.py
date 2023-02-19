import pandas as pd
import numpy as np
from SeriesFormatter import *

import plotly.express as px
import pandas as pd

from dash import Dash, dcc, html, Input, Output, State
from dash import dash_table



class SeriesSelection:
    app = Dash(__name__)
    def __init__(self):
        self._app = Dash(__name__)
        self._sf = SeriesFormatter()
        self._series = None
        self._regions = None
        self.load_options()
        self._series_options = [i for i in self._series.keys()]
        self._regions_options = ["%s - %s" % (i, self._regions[i]) for i in self._regions.keys()]
        self._selected_series = dash_table.DataTable(pd.DataFrame(columns=["Series", "Region"]).to_dict())

        self._text = html.Label("Null")
        self.select_button = html.Button("Add Series", id="select")

    def build_view(self):


        series_dropdown = dcc.Dropdown(options=self._series_options, value="Choose series...")
        regions_dropdown = dcc.Dropdown(options=self._regions_options, value="Choose region...")
        self._app.layout = html.Div(children=[
            series_dropdown,
            regions_dropdown,
            self._selected_series
        ])


    def refresh_view(self):
        @self.app.callback(
            Output(),
            Input('select'),
            State('input-on-submit', 'value')
        )
        def refresh():

            series_dropdown = dcc.Dropdown(options=self._series_options, value="Choose series...")
            regions_dropdown = dcc.Dropdown(options=self._regions_options, value="Choose region...")

            self._app.layout = html.Div(children=[
                series_dropdown,
                regions_dropdown
            ])


    def load_options(self):
        with open("series_data.json", "r") as file:
            self._series = json.load(file)
        with open("regions_data.json", "r") as file:
            self._regions = json.load(file)


    @property
    def sf(self):
        return self._sf


    def enable_view(self):
        self._app.run_server(port=8001)


def main():
    ss = SeriesSelection()
    sf = SeriesFormatter()
    sf.get_series_id()
   # sf.pull_compile_data()

    ss._sf = sf
    ss.load_options()
    ss.build_view()
    ss.enable_view()


if __name__ == "__main__":
    main()