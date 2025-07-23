import pandas as pd

class Loader:

    def __init__(self, path_to_csv):
        self.DF = self.from_csv_to_df(path_to_csv)

    def from_csv_to_df(self, path):
        df = pd.read_csv(path)
        return  df

