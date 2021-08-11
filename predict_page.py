import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data=pickle.load(file)
    return data

data=load_model()
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]



def show_predict_page():
    from PIL import Image
  


    #audio_file=open("music_corporate.mp3","rb").read()
    #st.audio(audio_file,format='audio/mp3',start_time=0)

    st.sidebar.header('Ezzedine Fitouri')
    img = Image.open('Image2.png')
    st.sidebar.image(img,width=200,caption='Pharmaceutical Marketing- Business analytics')
    st.sidebar.info('Driven by a taste for challenge, I am a dynamic,enthusiastic, adaptable person. My training and my various professional experiences during more than 14 years in the pharmaceutical field have allowed me to develop a real business sense and an attention to detail. My passion for new technologies and data have led me to start an intelligence artificial degree. My interpersonal and writing skills allow me to clearly communicate my ideas and be a force of conviction. I advocate teamwork because it is the prerequisite for meeting all challenges...')
    
    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)

    expericence = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")