import streamlit as st
import functions_web
import os

print(os.getcwd())


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions_web.write_file(todos)


todos = functions_web.open_file()

st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f'checklist-{index}')
    if checkbox:
        todos.pop(index)
        functions_web.write_file(todos)
        st.experimental_rerun

st.text_input(label='Enter a todo', placeholder='Add new todo..',
              on_change=add_todo, key='new_todo')

st.session_state
