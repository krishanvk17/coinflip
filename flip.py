import streamlit as st
import random

st.title("Coin flip!")
st.write("This is Coin Flip, a simple coin flipper, it lands on heads or tails.")
num=random.randint(1,2)
if st.button("Flip!"):
  if num==1:
    st.write("Heads!")
  else:
    st.write("Tails!")


  
