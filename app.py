import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('house_price_model.pkl')

# Title
st.title("🏠 House Price Prediction")

st.write("Enter house details below:")

# User inputs
area = st.number_input("Living Area")
garage = st.number_input("Garage Cars")
basement = st.number_input("Basement Area")
rooms = st.number_input("Total Rooms")
age = st.number_input("House Age")

# Prediction
if st.button("Predict Price"):

    features = np.array([[area, garage, basement, rooms, age]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")