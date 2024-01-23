"""Manages password.

The password generator uses this library:
    https://github.com/gabfl/password-generator-py/
"""


import streamlit as st
from modules.password import get_password_generator, get_credential_vault
from modules.auth import get_auth, get_login
from passwordgenerator import pwgenerator


if 'authentication_status' not in st.session_state:
    st.session_state.authentication_status = None

if 'pw' not in st.session_state:
    st.session_state.pw = pwgenerator.generate()


def main():
    st.title('Password Safe')

    tab1, tab2 = st.tabs(['Generator', 'Manager'])

    # Free
    with tab1:
        with st.container(border=True):
            st.subheader('Password Generator')
            st.markdown('Generates password randomly.')
            get_password_generator()

    # Needs Login
    with tab2:
        if st.session_state.authentication_status is None:
            authenticator = get_auth()
            get_login(authenticator)
            
        if st.session_state.authentication_status:
            with st.container(border=True):
                st.subheader('Secret Vault')
                get_credential_vault()


if __name__ == '__main__':
    main()
