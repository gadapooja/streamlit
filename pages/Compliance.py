import streamlit as st
import pandas as pd
import os

st.title('Compliance Portal')
st.text('Use this page to upload the monthly file')

uploaded_file = st.file_uploader('Upload a CSV',type=['csv','xlsx'])
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe.head())
    
else:
    st.error('Incorrect format of file')