import streamlit as st
from main import main

st.title('InNsighter')
data = st.text_input(label="News Info")
if data:
    st.write(main(data))
