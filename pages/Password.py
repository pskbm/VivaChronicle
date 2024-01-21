"""Manages password.

The password generator uses this library:
    https://github.com/gabfl/password-generator-py/
"""


import streamlit as st
from passwordgenerator import pwgenerator
from modules.password import spacer


if 'pw' not in st.session_state:
    st.session_state.pw = pwgenerator.generate()


def gen_pass_cb():
    """Generates random password."""
    st.session_state.pw = pwgenerator.generate()


st.title('Password Generator')

st.markdown('Generates password randomly.')

# Creates 2 widgets along the row.
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

