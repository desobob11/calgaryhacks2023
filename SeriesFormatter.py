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

class SerialFormatter:

    def __init__(self):
        #TODO: hardcode for now, REMEMBER THIS SHOULD BE INPUT BY JSON AT THE END
       #self._series = None
        self._series = {"Forest area (% of land area)" : ["AFE", "AFW"]}
        self._dfs = {}
        self._series_ids = None
        #self._region_meta = None
        self._df = None

    def get_series_id(self) -> None:
        print(self._series.keys())
        with open("series_data.json", "r") as file:
            json_map = json.load(file)
        self._series_ids = {}
        for i in self._series.keys():
            self._series_ids[i] = json_map[i]





    def pull_compile_data(self):

        for name in self._series_ids:
            self._dfs[name] = wbgapi.data.DataFrame(self._series_ids[name], self._series[name]).transpose()






    #def pull_series(self):
     #   df = pd.DataFrame()
      #  for i in self._series:






def main():

    sf = SerialFormatter()

    sf.get_series_id()
    sf.pull_compile_data()
    df = None
    for i in sf._dfs:
        #print(sf._dfs[i])
        df = sf._dfs[i]
    plt.plot(df.index, df["AFW"])
    plt.plot(df.index, df["AFE"])
    plt.show()


if __name__ == "__main__":
    main()


