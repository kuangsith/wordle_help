import streamlit as st
import pandas as pd
import wordle_help

st.header("Wordle Helping tool! Never go over 6 again!")



col1, col2, = st.columns(2)
with col1:
    st.write("List of best words to guess")
    st.dataframe(wordle_help.df)

with col2:
    st.write("List of possible answers.")
    st.dataframe(wordle_help.dfremain)