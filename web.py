import streamlit as st
from modules import functions

todos = functions.get_todos()

# Script is executed from top to bottom everytime the page is refreshed

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")
