import uvicorn
from fastapi import FastAPI, Query, HTTPException
import requests
from urllib3.exceptions import NameResolutionError

from classifier import Classifier
from validator import Validator

app = FastAPI()
get_dict_url = "http://model_generator:5000/get_dict"
query_url ="http://0.0.0.0:8080/predict?age=senior&income=medium&student=no&credit_rating=excellent"


@app.get("/predict")
def predict_by_query(age: str, income: str, student: str, credit_rating: str):

    # get the dict from the model container
    try:
        resp = requests.get(get_dict_url)  # get the dict from model container
        dict_prob = resp.json()
    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Error fetching dict from model-generator: {e}")

    # create the query dict
    query_dict = {
        "age": age,
        "income": income,
        "student": student,
        "credit_rating": credit_rating
    }

    # make the classifier and return answer
    validated_df = Validator(None, dict_prob).df
    classifier = Classifier(validated_df)
    prediction = classifier.probability(query_dict)
    return {"prediction": prediction}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
