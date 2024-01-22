"""Supports password page."""


import streamlit as st
from passwordgenerator import pwgenerator
import pandas as pd


def spacer(height: int = 30):
    """Used to align widgets horizontally."""
    return st.write(f'<div style="height: {height}px;"></div>', unsafe_allow_html=True)


if 'pw' not in st.session_state:
    st.session_state.pw = pwgenerator.generate()


def gen_pass_cb():
    """Generates random password."""
    st.session_state.pw = pwgenerator.generate()


def get_password_generator():
    cols = st.columns([1, 5])

    with cols[0]:
        spacer(height=29)
        st.button('Generate', type='primary', on_click=gen_pass_cb)

    with cols[1]:
        st.text_input(
            'Random password',
            value=st.session_state.pw,
            key='rpw_k',
            label_visibility='hidden'
        )


def get_credential_vault():
    df = pd.DataFrame(
        {
            'Name': ['Gregg Mesa', 'Linda Saturan'],
            'Username': ['dami', 'sikat'],
            'Email': ['greggmesa@gmail.com', 'lindasat@gmail.com'],
            'Url': ['https://streamlit.io/', 'https://www.facebook.com/'],
            'Password': ['Dummies-Chasers.Recoded:594', 'Henna%474-Gulfs;Quickens']
        }
    )

    st.data_editor(
        df,
        column_config={
            'url': st.column_config.LinkColumn(),
            # 'username': st.column_config.TextColumn(disabled=True),
            # 'category': st.column_config.SelectboxColumn(options=['personal', 'work', 'others']),
        },
        use_container_width=True,
        hide_index=True
    )
