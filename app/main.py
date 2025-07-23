from fastapi import FastAPI
from loader import Loader
from cleaner import Cleaner
from trainer import Trainer


FILE_PATH = "../data/data_for_NB_buys_computer-Sheet1.csv"
TARGET_COL = "Buy_Computer"

app = FastAPI()

@app.get("/dict")
def get_dict():
    df = Loader(FILE_PATH).from_csv_to_df(FILE_PATH)
    cleaned = Cleaner(df, TARGET_COL).df
    trainer = Trainer(cleaned, TARGET_COL)
    return trainer.result_dict
