import streamlit as st
from modules.todo import Todo


if 'authentication_status' not in st.session_state:
    st.session_state.authentication_status = None


# Switch page
if st.session_state.authentication_status is None:
    st.switch_page('./pages/Authentication.py')


st.title('Todo')

if st.session_state.authentication_status:
    st.write(f'username: **{st.session_state.username}**')

    todo = Todo(st.session_state.username)

    todo.get_description()

    todo.get_table()

