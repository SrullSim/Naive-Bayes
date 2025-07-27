from fastapi import FastAPI, Query, HTTPException
import requests
from classifier import Classifier
from validator import Validator

app = FastAPI()
url = "http://localhost:8000/predict?age=senior&income=medium&student=no&credit_rating=excellent"


@app.get("/predict")
def predict_query(age: str, income: str, student: str, credit_rating: str):

    # get the dict from the model container
    try:
        resp = requests.get(url)  # הפניה לקונטיינר ראשון הפועל ב-5000
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
