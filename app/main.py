from loader import Loader
from cleaner import Cleaner
from trainer import Trainer
from validator import Validator
from classifier import Classifier

FILE_PATH = r"C:\Users\User\Desktop\DATA\Naive-Bayes\data_for_NB_buys_computer-Sheet1.csv"
TARGET_COL = "Buy_Computer"
QUERY_DICT = { "age":"senior","income":"medium","student":"no","credit_rating":"excellent"}

def manager():
    # load the file to df
    df = Loader(FILE_PATH).from_csv_to_df(FILE_PATH)

    # clean the data
    clean_data = Cleaner(df,TARGET_COL).df

    # train the model & return dict
    trainer = Trainer(clean_data,TARGET_COL)
    dict_prob = trainer.result_dict

    # check the model validation
    validator = Validator(trainer, dict_prob).df

    # the classifier

    ans = Classifier(validator, QUERY_DICT).probability()
    return ans

print(manager())






