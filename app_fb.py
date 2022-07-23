import pandas as pd 
import streamlit as st


primaryColor = "#575fe8"
backgroundColor = "#f5f7f3"
secondaryBackgroundColor = "#c9eab8"
textColor = "#262730"
font = "sans serif"

data=pd.read_csv("fb_result.csv")
data=data.drop(["Unnamed: 0"],axis=1)
st.title("Facebook Data")
st.dataframe(data)

st.markdown(("""___"""))

_id=str(data["id"][0])
st.write("The ID is ",_id)
st.markdown(("""___"""))

f_name=str(data["first_name"][0])
st.write("First Name : ",f_name)
st.markdown(("""___"""))

l_name=str(data["last_name"][0])
st.write(" Last_Name : ",l_name)
st.markdown(("""___"""))


name=str(data["name"][0])
st.write("The name is ",name)
st.markdown(("""___"""))

email=str(data["email"][0])
st.write("The email is ",email)

