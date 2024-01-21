"""Supports authentication page."""


import streamlit as st
import streamlit_authenticator as stauth


def get_auth():
    return stauth.Authenticate(
        dict(st.secrets['credentials']),
        st.secrets['cookie']['name'],
        st.secrets['cookie']['key'],
        st.secrets['cookie']['expiry_days'],
        st.secrets['preauthorized']
    )
