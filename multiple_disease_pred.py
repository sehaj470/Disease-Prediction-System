# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:03:36 2024

@author: asus
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

import numpy as np


# loading the models

heart_model = pickle.load(open('C:/Users/sehaj/OneDrive/Documents/EVERYTHING/projects/Sehaj & mandeep/models machine learning/heart_model.sav', 'rb'))

diabetes_model = pickle.load(open('C:/Users/sehaj/OneDrive/Documents/EVERYTHING/projects/Sehaj & mandeep/models machine learning/diabetes_model_2.sav', 'rb'))

parkinsons_model = pickle.load(open('C:/Users/sehaj/OneDrive/Documents/EVERYTHING/projects/Sehaj & mandeep/models machine learning/parkinsons_model.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Heart Disease',
                            'Diabetes',
                            'Parkinsons'],
                           
                           icons = ['heart', 'activity', 'virus'],
                           
                           default_index = 0)
    

# heart disease prediction page
if (selected == 'Heart Disease'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    # getting input data from user
    # columns for input fields
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
    
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dL')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dL')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope  = st.text_input('slope of the peak exercise ST segment')
    
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    
    # code for prediction
    heart_diagnosis = ''
    
    # creating button for prediction
    if st.button('Check for Result'):
        
        try:
            # Convert inputs to numeric
            inputs = [int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg), int(thalach), int(exang), float(oldpeak), int(slope), int(ca), int(thal)]
            heart_prediction = heart_model.predict([inputs])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has Heart Disease'

                
            else:
                heart_diagnosis = 'The person has Healthy Heart'
        except ValueError:
            heart_diagnosis = 'Error: Please ensure all input fields are numeric.'

    
    st.success(heart_diagnosis)
    
    
    
    
    
    
if (selected == 'Diabetes'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting input data from user
    # columns for input fields
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
       # Pregnancies = st.slider('Preganancies',0, 17, 3)
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        
    with col3:
        BMI = st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of person')
    
       
    
    # code for prediction
    diab_diagnosis = ''
    
    # creating button for prediction
    if st.button('Check for Result'):
        
        try:
            inputs1 = [int(Pregnancies), int(Glucose), int(BloodPressure), int(SkinThickness), int(Insulin), float(BMI), float(DiabetesPedigreeFunction), int(Age)]
            diab_prediction = diabetes_model.predict([inputs1])
    
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person has Diabetes'
            else:
                diab_diagnosis = 'The person is not Diabetic'
        except ValueError:
            diab_diagnosis = 'Error: Please ensure all input fields are numeric.'

    
    st.success(diab_diagnosis)



if (selected == 'Parkinsons'):
    
    # page title
    st.title('Parkinsons Prediction using ML')
    
    # getting input data from user
    # columns for input fields
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        Fo = st.text_input("MDVP-Fo(Hz)")
        
    with col2:
        Fhi = st.text_input('MDVP-Fhi(Hz)')
        
    with col3:
        Flo = st.text_input('MDVP-Flo(Hz)')
    
    with col4:
        Jitter_percent = st.text_input('MDVP-Jitter(%)')
        
    with col5:
        Jitter_abs = st.text_input('MDVP-Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP-RAP')
        
    with col2:
        PPQ = st.text_input('MDVP-PPQ')
        
    with col3:
        DDP = st.text_input('Jitter-DDP')
    
    with col4:
        Shimmer = st.text_input('MDVP-Shimmer')
        
    with col5:
        Shimmer_db = st.text_input('MDVP-Shimmer(dB)')
        
    with col1:
        APQ3  = st.text_input('Shimmer-APQ3')
    
    with col2:
        APQ5 = st.text_input('Shimmer-APQ5')
        
    with col3:
        APQ = st.text_input('MDVP-APQ')
        
    with col4:
        DDA = st.text_input('Shimmer-DDA')
    
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
    
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
    
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE  = st.text_input('PPE')
    
    
    
    
    
    # code for prediction
    parkinson_diagnosis = ''
    
    # creating button for prediction
    if st.button('Check for Result'):
        
        try:
            # Convert inputs to numeric
            inputs = [float(Fo), float(Fhi), float(Flo), float(Jitter_percent), float(Jitter_abs), float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_db), float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]
            parkinsons_prediction = parkinsons_model.predict([inputs])

            if parkinsons_prediction[0] == 1:
                parkinson_diagnosis = 'The person has Parkinsons Disease'

            else:
                parkinson_diagnosis = 'The person does not have Parkinsons Disease'
        except ValueError:
            parkinson_diagnosis = 'Error: Please ensure all input fields are numeric.'

    
    st.success(parkinson_diagnosis)
 




