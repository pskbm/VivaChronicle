import streamlit as st


def spacer(height: int = 30):
    """Used to align widgets horizontally."""
    return st.write(f'<div style="height: {height}px;"></div>', unsafe_allow_html=True)
