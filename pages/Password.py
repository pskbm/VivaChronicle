import streamlit as st
from passwordgenerator import pwgenerator
import pyperclip
from modules.password import spacer


if 'pw' not in st.session_state:
    st.session_state.pw = pwgenerator.generate()


st.title('Password Generator')


def gen_pass_cb():
    st.session_state.pw = pwgenerator.generate()


def pass_copy_cb():
    pyperclip.copy(st.session_state.pw)


cols = st.columns([1, 4, 2])

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

with cols[2]:
    spacer(height=29)
    st.button('Copy', type='secondary', on_click=pass_copy_cb)

