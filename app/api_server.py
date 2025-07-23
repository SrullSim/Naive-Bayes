from fastapi import FastAPI, HTTPException, Query
from loader import Loader
from cleaner import Cleaner
from trainer import Trainer
from validator import Validator
from classifier import Classifier
import uvicorn

FILE_PATH = r"C:\Users\User\Desktop\DATA\Naive-Bayes\data_for_NB_buys_computer-Sheet1.csv"
TARGET_COL = "Buy_Computer"

#  FASTAPI
app = FastAPI()
#

# run the model
def run_model(query_dict: dict) -> float:
    df = Loader(FILE_PATH).from_csv_to_df(FILE_PATH)
    cleaned = Cleaner(df, TARGET_COL).df
    trainer = Trainer(cleaned, TARGET_COL)
    dict_prob = trainer.result_dict
    validated_df = Validator(trainer, dict_prob).df
    result = Classifier(validated_df, query_dict).probability()
    return result

@app.get("/predict")
def predict(
    age: str = Query(...),
    income: str = Query(...),
    student: str = Query(...),
    credit_rating: str = Query(...)
):
    try:
        query_dict = {
            "age": age,
            "income": income,
            "student": student,
            "credit_rating": credit_rating
        }
        result = run_model(query_dict)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"שגיאה: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
