import streamlit as st
from modules.home import CONTENT


if 'authentication_status' not in st.session_state:
    st.session_state.authentication_status = None


def main():
    st.header('Main')

    # Switch page
    if st.session_state.authentication_status is None:
        st.switch_page('./pages/Authentication.py')


    if st.session_state["authentication_status"]:
        st.markdown(CONTENT)


if __name__ == '__main__':
    main()
