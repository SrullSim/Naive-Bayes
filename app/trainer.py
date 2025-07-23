

class Trainer:

    def __init__(self, df, target_column):
        self.DF = df
        self.target_column = target_column
        self.result_dict ={}


    @staticmethod
    def unique_values(dataframe, column):
        return dataframe[column].unique()

    @staticmethod
    def amount_of_unique_values(dataframe, column, value):
        return float(dataframe.loc[dataframe[column] == value, column].count())

    @staticmethod
    def amount_of_all_values(dataframe):
        return float(dataframe.shape[0])

    def all_columns(self, classifier):
        columns = self.DF.columns
        return [col for col in columns if col != classifier]

    def split_dataframe_by_value(self, column, value):
        return self.DF.groupby(column).get_group(value)

    def dict_class(self):
        class_dict = {}
        all_values = self.amount_of_all_values(self.DF)
        for val in self.unique_values(self.DF,self.target_column):
            unique_values = self.amount_of_unique_values(self.DF,self.target_column,val)
            class_dict[val] = unique_values / all_values
        return class_dict

    def dict_values(self):
        result = {}
        for val in self.unique_values(self.DF, self.target_column):
            split_df = self.split_dataframe_by_value(self.target_column, val)
            column = self.all_columns(self.target_column)
            col_dict = {}
            for col in column:
                count_val = self.amount_of_all_values(split_df)
                unique_val = self.unique_values(self.DF, col)
                split_unique_val = self.unique_values(split_df, col)
                inner_dict = {}
                if len(unique_val) == len(split_unique_val):
                    for value in unique_val:
                        value_count = self.amount_of_unique_values(split_df, col, value)
                        inner_dict[value] = value_count / count_val
                else:
                    count_val += len(unique_val)
                    for value in unique_val:
                        value_count = self.amount_of_unique_values(split_df, col, value) + 1
                        inner_dict[value] = value_count / count_val
                col_dict[col] = inner_dict
            result[val] = col_dict
        # pprint(result)
        self.result_dict = result
        return result

