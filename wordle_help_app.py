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
dfremain = df.loc[remaining].sort_values(by='Expected entropy',ascending=False)


col1, col2, col3 = st.columns(2)
with col1:
    guess = st.text_input('Your guess')
    result = st.text_input('Color result','bbbbb')
    updateresult = st.button('Update')

with col2:
    st.write("List of best words to guess")
    st.dataframe(df)

with col3:
    st.write("List of possible answers.")
    st.dataframe(dfremain)