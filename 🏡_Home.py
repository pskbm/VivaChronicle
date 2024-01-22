import streamlit as st
from modules.home import CONTENT


st.set_page_config(
    page_title='VivaChronicle',
    layout='centered',
    initial_sidebar_state='expanded',
    page_icon=':art:',
    menu_items={
        'Report a bug': 'https://github.com/fsmosca/stauth-chat/issues'
    }
)


def main():
    st.title('Home')
    st.markdown(CONTENT)


if __name__ == '__main__':
    main()
