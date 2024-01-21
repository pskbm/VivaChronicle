"""Manages user authentication."""


import streamlit as st
from modules.auth import get_auth, get_login, get_register, get_logout


st.title('Authentication')

authenticator = get_auth()

tab1, tab2, tab3 = st.tabs(['Login', 'Register', 'Logout'])

with tab1:
    get_login(authenticator)

with tab2:
    st.error('This is not supported yet.')
    get_register(authenticator)

with tab3:
    if st.session_state["authentication_status"]:
        get_logout(authenticator)
