import streamlit as st
import datetime
import requests

'''
# Taxi Fare Prediction
'''

date = st.date_input(label='Enter the Date',
                  value=datetime.datetime.today())
time = st.time_input(label='Enter the Time',
                  value=datetime.datetime.now().time())
pickup_datetime = str(date) +' '+ str(time)
pickup_lon = st.number_input('pickup longitude')
pickup_lat = st.number_input('pickup latitude')
dropoff_lon = st.number_input('dropoff longitude')
dropoff_lat = st.number_input('dropoff latitude')
passenger_count = st.number_input('passenger count', min_value = 1, max_value = 7, step = 1)

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

if st.button('Estimated fare'):
    params_dict = {
        'pickup_datetime':pickup_datetime,
        'pickup_longitude':pickup_lon,
        'pickup_latitude':pickup_lat,
        'dropoff_longitude':dropoff_lon,
        'dropoff_latitude':dropoff_lat,
        'passenger_count':passenger_count
        }
    response = requests.get('https://taxifare.lewagon.ai/predict', params=params_dict).json()

    st.write('The estimated fare is:',response['prediction'])
