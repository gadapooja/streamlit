import streamlit as st
import pandas as pd
import os
import datetime
import subprocess as sp
import bcpy
import sys

st.title('Adding users to the distribution lists')
st.text('This step is part of the on-boarding process and lets you add users to the required distribution lists')
st.text('To perform this task successfully you need to provide a csv file with that contains the user\'s email address and distribution list name/email address')
st.text('The fils shoud look like this')
# example_csv_file = 'C:\Users\pooja.gada\floatspec_code\streamlit\all_employyes.csv'
# st.write(pd.read_csv(example_csv_file).head())

uploaded_file = st.file_uploader('Upload a CSV',type=['csv','xlsx'])
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe.head())
    
else:
    st.error('Incorrect format of file')

now = datetime.datetime.now()
Day = now.strftime("%Y-%m-%d")


def add_members_to_dl():
    st.write("\nAdding new members to distribution lists from the csv file at location C:\projects\data\\add_members.csv")
    choice = st.selectbox('Pick one',['Yes','No'])
    if choice == "Yes":
        st.write('Members are getting added to distribution lists')
        out = sp.run([r'C:\\Users\\pooja.gada\\floatspec_code\\streamlit\\streamlit\\member.bat'] , stdout=sp.PIPE, stderr = sp.PIPE, text=True)
        
        if out.stderr:
            st.write(out.stderr)
            #logging.info(f'{out.stderr}')
            text_msg = f'\n New Interns were not added to distribution lists on {Day}.\n Please check attached log file for more details.'
            #gm.send_mail_via_smtp(configparser.sender_address,configparser.alert_email,etl_name +  ' Intern unsuccessful',text_msg,log_file_name)
            #sys.exit(1)
        else:
            # print(out.stdout)
            # logging.info(out.stdout)
            index = out.stdout.find('Successfully')
            st.write(out.stdout[index:])
            # logging.info(out.stdout[index:])
            # gm.pp('\n Members were added on ',Day)
            st.write(f'\n Members were added on {Day}')
            # text_msg = f'\n New Interns were added to distribution lists on {Day}.\n Please check attached log file for more details.'
            # gm.send_mail_via_smtp(configparser.sender_address,configparser.alert_email,etl_name +  ' Intern successful',text_msg,log_file_name)
        
    elif choice == "No":
        #gm.pp('\n Did not add members to distribution lists. Going back to menu \n ')
        st.write(f'\n Did not add members to distribution lists. Going back to menu \n ')
add_members_to_dl()