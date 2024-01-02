from fastapi import FastAPI
import pickle
import uvicorn
from pydantic import BaseModel
import numpy as np

# Define a request model
class RequestModel(BaseModel):
    features: list

# Initialize the FastAPI app
app = FastAPI()  # Note: FastAPI should be capitalized

# Load your trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Define a predict endpoint
@app.post("/predict")
def predict(request: RequestModel):
    features = np.array(request.features).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": prediction.tolist()}  # Convert numpy array to list
