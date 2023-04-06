import streamlit as st
import pandas as pd
from PIL import Image

rerunrequest = False
st.write("""
# Don't be the last: the stone picking game!
""")

#df = pdf.read_csv("dat.csv")
#st.bar_chart(df)

if 'count' not in st.session_state:
    st.session_state.count = 20
if 'rule' not in st.session_state:
    st.session_state.rule = '1,2,3'
if 'temp' not in st.session_state:
    st.session_state.temp = '1,2,3'

with st.expander("Setting"):


    num = st.slider("Number of stones: ",min_value=10,max_value=50)
    

    st.write("How many stones can a player take in a turn?")
    xol1,xol2,xol3 = st.columns(3)
    with xol1:
        but12 = st.button("1,2")
    with xol2:
        but123 = st.button("1,2,3")
    with xol3:
        but1234 = st.button("1,2,3,4")

    
    if but12:
        st.session_state.temp = '1,2'
    if but123:
        st.session_state.temp = '1,2,3'
    if but1234:
        st.session_state.temp = '1,2,3,4'



    st.write("Reset the game to "+str(num)+" stones, and the rule to able to take " +st.session_state.temp + " stones.")
    resetbut = st.button("Reset")
    if resetbut:
        st.session_state.count = num
        st.session_state.rule = st.session_state.temp

#color = st.color_picker("What color do we want?",'#00f900')





minus1=False
minus2=False
minus3=False
minus4=False

st.header("Gameplay")
st.write("The current rule is you may take "+st.session_state.rule+" stones.")
st.write("How many stones are you taking?")
col1,col2,col3,col4 = st.columns(4)
with col1:
    if st.session_state.count >=1:
        minus1= st.button("-1")
with col2:
    if st.session_state.count >=2:
        minus2= st.button("-2")
with col3:
    if st.session_state.count >=3 and (st.session_state.rule == '1,2,3' or st.session_state.rule == '1,2,3,4'):
        minus3= st.button("-3")
with col4:
    if st.session_state.count >=4 and st.session_state.rule == '1,2,3,4':
        minus4= st.button("-4")

if minus1:
    st.session_state.count = st.session_state.count-1
    rerunrequest = True

if minus2:
    st.session_state.count = st.session_state.count-2
    rerunrequest = True

if minus3:
    st.session_state.count = st.session_state.count-3
    rerunrequest = True

if minus4:
    st.session_state.count = st.session_state.count-4
    rerunrequest = True


st.write("The number is ")
st.title(str(st.session_state.count))
img = Image.open("peb.png")

#printing stones
s1,s2,s3,s4,s5,e1,s6,s7,s8,s9,s10 = st.columns(11)

n1 = (st.session_state.count+9)//10
n2 = (st.session_state.count+8)//10
n3 = (st.session_state.count+7)//10
n4 = (st.session_state.count+6)//10
n5 = (st.session_state.count+5)//10
n6 = (st.session_state.count+4)//10
n7 = (st.session_state.count+3)//10
n8 = (st.session_state.count+2)//10
n9 = (st.session_state.count+1)//10
n10 = (st.session_state.count)//10

#st.write(str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9)+str(n10))

#do it column by column
with e1:
    st.write(" ")

with s1:
    for i in range(n1):
        st.image(img,width=60)

with s2:
    for i in range(n2):
        st.image(img,width=60)

with s3:
    for i in range(n3):
        st.image(img,width=60)

with s4:
    for i in range(n4):
        st.image(img,width=60)

with s5:
    for i in range(n5):
        st.image(img,width=60)

with s6:
    for i in range(n6):
        st.image(img,width=60)

with s7:
    for i in range(n7):
        st.image(img,width=60)

with s8:
    for i in range(n8):
        st.image(img,width=60)

with s9:
    for i in range(n9):
        st.image(img,width=60)

with s10:
    for i in range(n10):
        st.image(img,width=60)

if st.session_state.count == 0:
    st.write("The game is over. Please reset to game to restart. Thank you for playing.")

if rerunrequest:
    st.experimental_rerun()

#for i in range(st.session_state.count):
#    st.image(img,width=60)






#st.latex(r'''x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}''')

#st.latex(r'''
#    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#    \sum_{k=0}^{n-1} ar^k =
#    a \left(\frac{1-r^{n}}{1-r}\right)
#    ''')