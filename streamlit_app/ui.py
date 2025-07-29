import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Heart Attack Risk Predictor", layout="centered")

st.title("💓 Heart Attack Risk Prediction")
st.markdown("Provide your medical inputs to check your risk level.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=45)
sex = st.selectbox("Sex", options=[("Male", 1), ("Female", 0)])
cp = st.selectbox("Chest Pain Type (cp)", options=[0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", value=120)
chol = st.number_input("Cholesterol (chol)", value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[0, 1])
restecg = st.selectbox("Resting ECG (restecg)", options=[0, 1, 2])
thalach = st.number_input("Max Heart Rate (thalach)", value=150)
exang = st.selectbox("Exercise Induced Angina (exang)", options=[0, 1])
oldpeak = st.number_input("ST depression (oldpeak)", value=1.0, step=0.1)
slope = st.selectbox("Slope of ST segment (slope)", options=[0, 1, 2])
ca = st.selectbox("Number of vessels colored by fluoroscopy (ca)", options=[0, 1, 2, 3])
thal = st.selectbox("Thalassemia (thal)", options=[0, 1, 2, 3])

input_data = {
    "age": age,
    "trestbps": trestbps,
    "chol": chol,
    "thalach": thalach,
    "oldpeak": oldpeak,
    "cp": cp,
    "fbs": fbs,
    "exang": exang,
    "sex": sex[1],  # Use 1 for Male, 0 for Female
    "restecg": restecg,
    "slope": slope,
    "ca": ca,
    "thal": thal
}

if st.button("Predict"):
    try:
        response = requests.post("http://localhost:8000/predict", json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"🧠 Prediction: {'⚠️ At Risk' if result['prediction'] else '✅ No Risk'}")
            st.info(f"Probability: {result['probability_risk']}% Risk vs {result['probability_no_risk']}% No Risk")
        else:
            st.error("Failed to get a response from the API.")
    except Exception as e:
        st.error(f"Error: {e}")

