import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

def predict_datapoint():
    st.title('Predict Data Point')

    # User input fields
    gender = st.selectbox('Gender', ['Male', 'Female'])
    ethnicity = st.selectbox('Ethnicity', ['Group A', 'Group B', 'Group C', 'Group D', 'Group E'])
    parental_education = st.selectbox('Parental Education Level', ['Some high school', 'High school', 'Some college', 'Associate\'s degree', 'Bachelor\'s degree', 'Master\'s degree'])
    lunch = st.selectbox('Lunch', ['Standard', 'Free/reduced'])
    test_preparation_course = st.selectbox('Test Preparation Course', ['Completed', 'None'])
    reading_score = st.number_input('Reading Score', value=0)
    writing_score = st.number_input('Writing Score', value=0)

    if st.button('Predict'):
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=float(reading_score),
            writing_score=float(writing_score)
        )
        pred_df = data.get_data_as_data_frame()

        st.write("Before Prediction")
        predict_pipeline = PredictPipeline()
        st.write("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        st.write("After Prediction")
        st.write('Result:', results[0])

def main():
    st.set_page_config(page_title="Predict Data", page_icon=":bar_chart:", layout="wide")

    st.markdown('# Predict Data')
    predict_datapoint()

if __name__ == "__main__":
    main()
