import streamlit as st
import joblib
import pandas as pd 
from streamlit_option_menu import option_menu
from PIL import Image
import seaborn as sns
import base64
import pickle
import numpy as np


with st.sidebar:
    selected=option_menu(
    menu_title="Main Menu",
        options=['Home','Loan Prediction'],
        icons=['house','book'],
        styles={
            "container":{"background-color":"#EC7063"},
            "nav-link":{
                "font-size":"21px",
                "--hover-color":"#CB4335",
                "color":"317202A"
            },
            "nav-link-selected":{
                "background-color":"#F8F521"
            },
            "icon":{
                "font-size":"20px"
            },
        },
    )

if selected == 'Home':
    st.markdown("""
    <style>
    .big-font1{
    font-size:50px !important;
    color:red;
    text-align:center;
    font-weight:bold;
    
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font1"> WELCOME TO THE FINANCIAL RISK PREDICTION SYSTEM </p>',unsafe_allow_html=True)
    st.markdown(' <p class="paragraph"> The purpose of this system is to provide information about a banks customers so that machine learning models can be developed that can predict whether a particular customer will repay the loan or not.  </p>',
    unsafe_allow_html=True)
    file_=open("risk3.png","rb")
    contents=file_.read()
    data_url=base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="500" image-align="center"  alt="risk3">',
        unsafe_allow_html=True, )

    

if selected=='Loan Prediction':
    #image=Image.open('risk2.png')
    
    #st.image(image)

    st.markdown("""
    <style>
        .big-font1{
            font-size:50px !important;
            color:red;
            text-align:center;
            font-weight:bold;
    </style>
    """,unsafe_allow_html=True)
    loaded_model=pickle.load(open('credit_risk.sav','rb'))

    def risk_prediction(input_data):
    

        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)

        if (prediction[0] == 0):
            return 'Sorry Your Loan is Not Approved'
        else:
            return 'Congratulations ! Your Loan is Approved'
    def main(): 


        st.markdown("<h1 style='text-align: center; color: black;'>FINANCIAL RISK ANALYSIS SYSTEM</h1>", unsafe_allow_html=True)
        #getting the input data from the user
        co1,col2,col3,col4=st.columns(4)


        with co1:
            gender=st.selectbox('Enter Your Gender as Male:0 Female:1',(0,1),index=0)
            married=st.selectbox('Enter Marital Status No : 0  Yes : 1',(0,1))
            dependents=st.selectbox('Enter numbers of dependents',(0,1,2,3,4))

        with col2:
            education=st.selectbox('Enter Education Graduate:0, Non Graduate:1',(0,1))
            self_employed=st.selectbox('Enter Self Employed Status No:0, Yes:1',(0,1))
            applicant_income=st.number_input('Enter Your Income',min_value=0)


        with col3:
            co_applicant_income=st.number_input('Enter Co-Applicant Income',min_value=0)
            loan_amount=st.number_input('Enter Loan Amount',min_value=0)
            loan_amount_term=st.number_input('Enter Loan Amount Term in Days',min_value=0)

        with col4:
            credit_history=st.selectbox("Enter Credit History",(0,1),index=0)
            property_area=st.selectbox('Enter the Property Area Semi-Urban:0 , Urban: 1,  Rular:2 ',(0,1,2),index=0)
            

        
    
        #code for the prediction 
    
        diagnosis=''
    
    
        #creating a button for prediction 
        if st.button('Financial Risk Prediction Result'):
            diagnosis = risk_prediction([gender,married,dependents,education,self_employed,applicant_income,co_applicant_income,loan_amount,loan_amount_term,credit_history,property_area])
            st.success(diagnosis)
        

    
    if __name__ =='__main__':
        main()









