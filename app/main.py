from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the model pipeline
model = joblib.load("model/pipeline.joblib")


# Define request schema
class PatientData(BaseModel):
    age: int
    trestbps: int
    chol: int
    thalach: int
    oldpeak: float
    cp: int
    fbs: int
    exang: int
    sex: int
    restecg: int
    slope: int
    ca: int
    thal: int

@app.post("/predict")
def predict_heart_attack(data: PatientData):
    input_data = np.array([[data.age, data.trestbps, data.chol, data.thalach, data.oldpeak,
                            data.cp, data.fbs, data.exang, data.sex, data.restecg,
                            data.slope, data.ca, data.thal]])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    return {
        "prediction": int(prediction),
        "probability_no_risk": round(probability[0]*100, 2),
        "probability_risk": round(probability[1]*100, 2)
    }

