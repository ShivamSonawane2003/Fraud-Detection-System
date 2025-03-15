#!/usr/bin/env python
# coding: utf-8



# In[34]:


import streamlit as st
import pandas as pd
import joblib  # For loading models

# In[36]:


import streamlit as st
import pandas as pd
import joblib  # For saving/loading models

# Load the trained model
@st.cache_resource
def load_model():
    # Load the model from a .pkl file
    try:
        model = joblib.load('fraud_detection_model.pkl')  # Replace with your file path
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Function to make predictions
def predict_fraud(model, input_data):
    try:
        prediction = model.predict(input_data)
        return prediction
    except Exception as e:
        st.error(f"Error making prediction: {e}")
        return None

# Streamlit app
import streamlit as st
import numpy as np
import joblib  # To load the pre-trained model

# Load pre-trained model (replace 'fraud_model.pkl' with your file)
model = joblib.load('fraud_detection_model.pkl')

# Mock prediction function (replace with actual model logic)
def predict_fraud(features):
    # Replace this with your model's prediction logic
    prediction = np.random.choice([0, 1])  # Mock prediction (0 = Not Fraud, 1 = Fraud)
    return "Fraudulent" if prediction == 1 else "Not Fraudulent"

# Streamlit app
st.title("Fraud Detection System")

# Input fields
transaction_amount = st.number_input("Transaction Amount (INR)", min_value=1, step=1)
transaction_time = st.time_input("Transaction Time")
previous_fraud = st.selectbox("Previous Fraud History", ["No", "Yes"])

# Predict button
# Create empty columns for alignment
col1, col2, col3 = st.columns([34, 34, 34])  # Adjust column widths for alignment

with col2:
    if st.button("Check Fraud"):
    # Example feature array (replace with actual input feature processing)
        features = [transaction_amount,transaction_time.hour, previous_fraud,]
        prediction = predict_fraud(features)
        st.write(f"Prediction: **{prediction}**")

