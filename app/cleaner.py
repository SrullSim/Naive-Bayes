


class Cleaner:

    def __init__(self, df, target_column):
        self.df = df
        self.target_column = target_column
        self.clean_data()


    # clean none and duplicates
    def clean_data(self):
        """ clean the df from none and duplicates """
        self.df = self.df.dropna()
        self.df = self.df.drop_duplicates()





