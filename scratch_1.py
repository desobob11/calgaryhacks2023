import wbgapi
import wbgapi.series as wseries
import wbgapi.series_metadata as wsm
import wbgapi.time as wtime
import wbgapi.source as sources
import wbgapi.data as wdata
import json
import pandas as pd
import numpy as np

d = {}

with open("series_data.json", "r") as file:
    d = json.load(file)

print(len(d.keys()))