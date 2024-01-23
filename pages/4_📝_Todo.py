"""Manages todo app."""


import streamlit as st
from modules.todo import Todo
from modules.auth import get_auth, get_login


if 'authentication_status' not in st.session_state:
    st.session_state.authentication_status = None


st.title('Todo')

if 'authentication_status' not in st.session_state or st.session_state.authentication_status is None:
    st.error('Log in to access the Todo organizer')
    authenticator = get_auth()
    get_login(authenticator)

if st.session_state.authentication_status:    
    st.write(f'username: **{st.session_state.username}**')

    todo = Todo(st.session_state.username)
    todo.get_description()
    todo.get_table()
