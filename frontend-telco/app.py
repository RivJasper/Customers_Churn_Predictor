import streamlit as st
import pandas as pd
import requests

def run():
    with st.form(key='form_parameters'):
        param_1 = st.number_input('Customer ID', step = 1) # customerID
        param_2 = st.radio('Gender', ('Male', 'Female')) # gender
        param_3 = st.radio('Senior Citizen', ('Yes', 'No')) # SeniorCitizen
        if param_3 == 'Yes':
            param_3 = 1
        else:
            param_3 = 0
        param_4 = st.radio('Do you have a partner', ('Yes', 'No')) # Partner
        param_5 = st.radio('Do you have dependents ?', ('Yes', 'No')) # Dependents
        param_6 = st.number_input('How long have you been using this telco (months) ?', min_value = 0, max_value = 120, step = 1) # tenure
        param_7 = st.radio('Do you have a phone service ?', ('Yes', 'No')) # PhoneService
        param_8 = st.selectbox('Do you have multiple lines ?', ('Yes', 'No', 'No internet service')) # MultipleLines
        param_9 = st.radio('Internet Service', ('DSL','Fiber Optic', 'No')) # InternetService
        param_10 = st.selectbox('Online Security', ('Yes', 'No', 'No internet service')) # OnlineSecurity
        param_11 = st.selectbox('Online Backup', ('Yes', 'No', 'No internet service')) # OnlineBackup
        param_12 = st.selectbox('Device Protection', ('Yes', 'No', 'No internet service')) # DeviceProtection
        param_13 = st.selectbox('Technical Support', ('Yes', 'No', 'No internet service')) # TechSupport
        param_14 = st.selectbox('Streaming TV', ('Yes', 'No', 'No internet service')) # StreamingTV
        param_15 = st.selectbox('Streaming Movies', ('Yes', 'No', 'No internet service')) # StreamingMovies
        param_16 = st.selectbox('Contract Term', ('Month-to-month','One year', 'Two Year')) # Contract
        param_17 = st.radio('Do you have paperless billing ?', ('Yes', 'No')) # PaperlessBilling
        param_18 = st.selectbox('Payment Method', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)')) # PaymentMethod
        param_19 = st.number_input('Monthly Charges', min_value = 0, step = 1000) # MonthlyCharges
        param_20 = st.number_input('Total Charges', min_value = 0, step = 1000) # TotalCharges
        submitted = st.form_submit_button('Predict')
    
    # Create A New data
    data_inf = {
        'customerID' : param_1,
        'gender' : param_2,
        'SeniorCitizen' : param_3,
        'Partner' : param_4,
        'Dependents' : param_5,
        'tenure' : param_6,
        'PhoneService' : param_7,
        'MultipleLines' : param_8,
        'InternetService' : param_9,
        'OnlineSecurity' : param_10,
        'OnlineBackup' : param_11,
        'DeviceProtection' : param_12,
        'TechSupport' : param_13,
        'StreamingTV' : param_14,
        'StreamingMovies' : param_15,
        'Contract' : param_16,
        'PaperlessBilling' : param_17,
        'PaymentMethod' : param_18,
        'MonthlyCharges' : param_19,
        'TotalCharges' : param_20,
    }

    if submitted:
        # Show Inference DataFrame
        st.dataframe(pd.DataFrame([data_inf]))
        print('[DEBUG] Data Inference : \n', data_inf)
        
        # Predict
        URL = 'https://backend-telco-rivjasper.koyeb.app/predict'
        r = requests.post(URL, json=data_inf)

        if r.status_code == 200:
            res = r.json()
            st.write('## Prediction : ', res['label_names'])
            print('[DEBUG] Result : ', res)
            print('')
        else:
            st.write('Error with status code ', str(r.status_code))
        
if __name__ == '__main__':
    run()