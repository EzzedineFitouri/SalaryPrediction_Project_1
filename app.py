import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page


st.title("Web Application : ")
st.text('Analysis based on the Public 2020 Stack Overflow Developer Survey')
page = st.selectbox("Explore Or Predict developper salary", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
