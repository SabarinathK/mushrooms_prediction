import streamlit as st
import pandas as pd
from app_frame import app_frame
import joblib

st.set_page_config(page_title='Mushroom Prediction')
st.title('Mushroom Prediction 🍄')
st.subheader('Lets findout your Edible Mushroom here !!! 🤤')

upload_file=st.file_uploader('Choose a csv')
if upload_file:
    st.markdown('-----')
    data=pd.read_csv(upload_file)
    file=app_frame.data_clean(df=data)
    loaded_model = joblib.load(open("models/model.pkl", 'rb'))
    model=pd.DataFrame(loaded_model.predict(file))
    result=model.replace({0:'Edible' , 1:"Possion"})
    st.dataframe(result)    