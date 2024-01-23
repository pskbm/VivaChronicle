"""Supports password page."""


import streamlit as st
from passwordgenerator import pwgenerator
import pandas as pd


def spacer(height: int = 30):
    """Used to align widgets horizontally."""
    return st.write(f'<div style="height: {height}px;"></div>', unsafe_allow_html=True)


if 'pw' not in st.session_state:
    st.session_state.pw = pwgenerator.generate()

if 'secret_data' not in st.session_state:
    st.session_state.secret_data = []


def save_pass_cb():
    st.session_state.secret_data.append(
        {
            'Name': st.session_state.pass_name,
            'Username': st.session_state.pass_username,
            'Password': st.session_state.pass_password
        }
    )


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
    holder = st.empty()

    # Input form
    with st.expander('Input Form', expanded=False):
        with st.form('form_password'):
            st.text_input('Name', key='pass_name')
            st.text_input('Username', key='pass_username')
            st.text_input('Password', key='pass_password')
            st.form_submit_button('Save', on_click=save_pass_cb)

    if 'secret_data' in st.session_state:
        df = pd.DataFrame(st.session_state.secret_data)

        holder.data_editor(
            df,
            use_container_width=True,
            hide_index=True
        )
