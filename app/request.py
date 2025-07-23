
import requests

url = "http://localhost:8000/predict?age=senior&income=medium&student=no&credit_rating=excellent"


response = requests.get(url)
print(response.json())
