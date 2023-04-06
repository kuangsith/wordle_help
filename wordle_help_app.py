import streamlit as st
import pandas as pd
import wordle_help

st.header("Wordle Helping tool! Never go over 6 again!")

if 'df' not in st.session_state:
    st.session_state.df = wordle_help.df
if 'remaining' not in st.session_state:
    st.session_state.remaining = wordle_help.remaining

df = st.session_state.df
remaining = st.session_state.remaining


col1, col2, = st.columns(2)
with col1:
    st.write("List of best words to guess")
    st.dataframe(df)

with col2:
    st.write("List of possible answers.")
    dfremain = df.loc[remaining].sort_values(by='Expected entropy',ascending=False)
    st.dataframe(wordle_help.remaining)