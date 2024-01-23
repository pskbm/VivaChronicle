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


def get_login(authenticator):
    authenticator.login('Login', 'main')

    if st.session_state["authentication_status"]:
        pass  # st.write(f'Logged username: **{st.session_state.username}**')

    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

    else:
        st.error('Username/password is incorrect')


def get_register(authenticator):
    try:
        if authenticator.register_user('Register user', preauthorization=False):
            pass  # st.success('User registered successfully')
    except Exception as e:
        st.error(e)


def get_logout(authenticator):
    st.markdown(f'''Welcome **{st.session_state["name"]}** 	:thumbsup:''')
    authenticator.logout('Logout', 'main', key='unique_key')
    