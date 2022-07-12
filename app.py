
import streamlit as st

st.text('Welcome to the web application for ')

image = (r"C:\\Users\\pooja.gada\\Downloads\\pjt_logo.jpg")
st.image(image,caption = 'PJT Logo')
with st.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    submitted = st.form_submit_button("Login")
if submitted:
    if username == 'pooja.gada@pjtpartners.com':
        st.success("User logged in")
else:
    st.error('You do not have access to this webpage')
    st.stop()