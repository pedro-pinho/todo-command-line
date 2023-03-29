import streamlit as st
from modules import functions

todos = functions.get_todos()


def add_todo():
    local_todo = st.session_state["new_todo"]
    todos.append(local_todo + "\n")
    functions.write_todos(todos)


# Script is executed from top to bottom everytime the page is refreshed

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Add new todo", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo",
              label_visibility='hidden')
