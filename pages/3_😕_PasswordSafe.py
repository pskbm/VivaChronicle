"""Manages password.

The password generator uses this library:
    https://github.com/gabfl/password-generator-py/
"""


import streamlit as st
from modules.password import get_password_generator, get_credential_vault
from modules.auth import get_auth, get_login
from passwordgenerator import pwgenerator


if 'pw' not in st.session_state:
    st.session_state.pw = pwgenerator.generate()

st.title('Password Safe')

with st.container(border=True):
    st.subheader('Password Generator')
    st.markdown('Generates password randomly.')
    get_password_generator()


if 'authentication_status' not in st.session_state or st.session_state.authentication_status is None:
    st.error('Log in to access the password manager')
    authenticator = get_auth()
    get_login(authenticator)

if st.session_state.authentication_status:
    with st.container(border=True):
        st.subheader('Credential Vault')
        st.markdown('Store credentials.')
        get_credential_vault()
