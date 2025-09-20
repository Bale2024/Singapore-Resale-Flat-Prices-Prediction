import pandas as pd
import streamlit as st
import pickle 
import numpy as np

# Load models and encoders
model_sprf = pickle.load(open("modelxgb.pkl","rb"))
encoders   = pickle.load(open("encoders.pkl","rb"))
scaler     = pickle.load(open("scaler.pkl", "rb"))

# Method to give inputs for the User:
def get_user_inputs(encoders):
    
    town = st.selectbox("Town", encoders["town"].classes_)
    flat_type = st.selectbox("Flat Type", encoders["flat_type"].classes_)
    street_name = st.selectbox("Street Name", encoders["street_name"].classes_)
    floor_area_sqm = st.number_input("Floor Area (sqm)", min_value=20.0, max_value=200.0, step=1.0)
    flat_model = st.selectbox("Flat Model", encoders["flat_model"].classes_)
    lease_commence_date = st.number_input("Lease Commence Year", min_value=1960, max_value=2050, step=1)
    year = st.number_input("Transaction Year", min_value=1990, max_value=2050, step=1)
    month_num = st.number_input("Transaction Month (1-12)", min_value=1, max_value=12, step=1)
    min_storey_range = st.number_input("Min Storey", min_value=1, max_value=50, step=1)
    max_storey_range = st.number_input("Max Storey", min_value=1, max_value=50, step=1)
    remaining_lease_years = st.number_input("Remaining Lease (years)", min_value=0, max_value=99, step=1)
    
    return {
        "town": town,
        "flat_type": flat_type,
        "street_name": street_name,
        "floor_area_sqm": floor_area_sqm,
        "flat_model": flat_model,
        "lease_commence_date": lease_commence_date,
        "year": year,
        "month_num": month_num,
        "min_storey_range": min_storey_range,
        "max_storey_range": max_storey_range,
        "remaining_lease_years": remaining_lease_years
       }
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Predict Resale Price"])
if page == "Home":
    st.title("🏠 HDB Resale Price Prediction")
    st.markdown("Welcome to Flat Resale Prediction App!" \
          "This project aims to predict the **resale value of HDB flats** in Singapore.  Switch between the" \
          " tabs using options in the sidebar.")
    st.image("sing_flat.png", use_container_width=True, width=1)
elif page == "Predict Resale Price":
    st.title("Predict Flat Resale Price")    
    st.write("Choose the User Inputs below :")
    user_inputs = get_user_inputs(encoders)
    st.write("Note: Click on the Predict button to get Flat Resale Price")
    if st.button("Predict Price"):
        input_df = pd.DataFrame([user_inputs])
        # Apply encoders for categorical features
        for col in ["town", "flat_type", "street_name", "flat_model"]:
            input_df[col] = encoders[col].transform(input_df[col])
        
        # Scale 
        input_scaled = scaler.transform(input_df)

        # Predict resale price
        prediction = model_sprf.predict(input_scaled)[0]
        st.success(f"Estimated Resale Price : ${prediction:,.0f}")
        st.balloons()
