import streamlit as st

st.write("Write a 4 letter english word")

import enchant
dict = enchant.Dict("en_US")
word = input("Enter the word: ")
print(dict.check(word))
