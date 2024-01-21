"""Manages todo app."""


import streamlit as st
from modules.todo import Todo


if 'authentication_status' not in st.session_state:
    st.session_state.authentication_status = None


st.title('Todo')

if st.session_state.authentication_status is None:
    st.error('Goto Authentication page to update login status.')

if st.session_state.authentication_status:
    st.write(f'username: **{st.session_state.username}**')

    todo = Todo(st.session_state.username)

    todo.get_description()

    todo.get_table()

