import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data=pickle(file)
    return data

data=load_model()
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Ezzedine Fitouri Salary prediction app")
    st.write("""###we need information to predict the salary""")