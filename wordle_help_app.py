import streamlit as st
import pandas as pd
import wordle_help

st.header("Wordle Helping tool! Never go over 6 again!")

st.write("Here are the best words to guess")

st.dataframe(wordle_help.df)