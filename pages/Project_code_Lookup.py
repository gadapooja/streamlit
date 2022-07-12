import streamlit as st

st.header('Try to find if company exist in the database')


with st.form(key='my_form'):
    title = st.text_input('Compnay Name', 'Name')
    capiq = st.text_input('CapIQ Id', 'Capiq')
    submitted = st.form_submit_button("Search Database")
    if submitted:
            st.success("Found the company")
    else:
        st.warning('Did not find the company')