import streamlit as st
import pandas as pd
import wordle_help

st.header("Wordle Helping tool! Never go over 6 again!")


if 'df' not in st.session_state:
    st.session_state.df = pd.read_csv("start_entropyv2.csv",index_col=0)
if 'remaining' not in st.session_state:
    with open('listofwordlewords.txt', 'r') as f:
        all = [line.strip() for line in f.readlines()]
    st.session_state.remaining = all
if 'allguess' not in st.session_state:
    st.session_state.allguess = pd.DataFrame(data = [],columns = ['Guess','Result'])

df = st.session_state.df
remaining = st.session_state.remaining
allguess = st.session_state.allguess
dfremain = df.loc[remaining].sort_values(by='Expected entropy',ascending=False)
ent = wordle_help.entropy(remaining)
numposs = len(remaining)

with st.expander("How to use:"):
    st.write("List of best words to gues = list of all words you can put in as your guess. Note that most of the words on the list are not possible answers to wordle game. The list is sorted by the information you would gain by guessing that word.")


st.header("Current stats")
st.write(f"Current entropy is {ent:.3f} and number of possible answers is {numposs}")



col1, col2, col3 = st.columns(3)
with col1:
    guess = st.text_input('Your guess')
    result = st.text_input('Color result','bbbbb')
    updateresult = st.button('Update')

    st.write('Previous guess')
    st.dataframe(allguess)

with col2:
    st.write("List of best words to guess")
    st.dataframe(df)

with col3:
    st.write("List of possible answers.")
    st.dataframe(dfremain)

if updateresult:
    st.session_state.remaining = wordle_help.play_and_update_remaining(guess,result,remaining)
    st.session_state.df = wordle_help.update_entropy(df,st.session_state.remaining)
    allguess = allguess.append({'Guess':guess , 'Result' :result},ignore_index=True)
    st.session_state.allguess = allguess
    st.experimental_rerun()

resetplease = st.button('Reset')

if resetplease:
    st.session_state.df = pd.read_csv("start_entropyv2.csv",index_col=0)
    with open('listofwordlewords.txt', 'r') as f:
        all = [line.strip() for line in f.readlines()]
    st.session_state.remaining = all
    st.session_state.allguess = pd.DataFrame(data = [],columns = ['Guess','Result'])
    st.experimental_rerun()