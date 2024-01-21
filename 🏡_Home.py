import streamlit as st
from modules.home import CONTENT
from modules.auth import get_auth


st.set_page_config(
    page_title='VivaChronicle',
    layout='centered',
    initial_sidebar_state='expanded',
    page_icon=':art:',
    menu_items={
        'Report a bug': 'https://github.com/fsmosca/stauth-chat/issues'
    }
)


if 'authentication_status' not in st.session_state:
    st.session_state.authentication_status = None


def main():
    st.title('Home')

    if st.session_state.authentication_status is None:
        st.error('Goto Authentication page to update login status.')


    if st.session_state["authentication_status"]:
        st.markdown(CONTENT)


if __name__ == '__main__':
    main()
