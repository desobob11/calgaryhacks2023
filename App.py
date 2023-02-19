import wbgapi
import wbgapi.series as wseries
import wbgapi.series_metadata as wsm
import wbgapi.time as wtime
import wbgapi.source as sources
import wbgapi.data as wdata
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from SeriesFormatter import *



from dash import Dash, html, dcc
from dash import dash_table
import plotly.express as px
import pandas as pd



app = Dash(__name__)
html.Div.
app.layout = html.Div(children = [

    html.Div(children="Hello"),

    dash_table.DataTable()





])


app.run_server()





def main():
    sf = SeriesFormatter()
    sf.get_series_id()
    sf.pull_compile_data()

    df = {}

    for i in sf._dfs:
        df = sf._dfs[i]
    app.run_server()
    print(df)


if __name__ == "__main__":
    main()
