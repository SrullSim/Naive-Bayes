from classifier import Classifier

class Validator:

    def __init__(self,df, trained_data):
        self.trained_data = trained_data
        self.df = df


    def sample(self,fraction):
        return self.df.DF.sample(frac=fraction)

    @staticmethod
    def left_sample(sample,original):
        return original[~original.index.isin(sample.index)]

    @staticmethod
    def data_frame_to_dict(dataframe):
        return dataframe.to_dict('index')

    def validation(self):
        """ take a sample of data for train the model and check the result """
        right = 0
        wrong = 0
        test_sample = self.sample(0.7)
        original_dataframe = self.df.DF
        self.df.DF = test_sample

        # create dict for checking
        trial_data = self.left_sample(test_sample,original_dataframe)
        probability = Classifier(self.df)
        for k,v in self.data_frame_to_dict(trial_data.drop(self.df.column_to_work_on, axis=1)).items():
            if str(probability.probability(v)) == str(trial_data.loc[k,self.df.column_to_work_on]):
                right += 1
            else:
                wrong += 1

        return right / (right + wrong)

    def is_valid_model(self):
        pass
