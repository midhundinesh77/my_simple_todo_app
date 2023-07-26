import streamlit as st
import functions

todos = functions.get_todos()


def add_new_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("To Ao App")
st.text("To do app for increasing productivity")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=index)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()
st.text_input(
    label="", placeholder="Add a new todo", on_change=add_new_todo, key="new_todo"
)
