import subprocess
import sys

import streamlit as st
import pyperclip


def copy_to_clipboard(text):
    if sys.platform == "linux" or sys.platform == "linux2":
        # Linux        
        p = subprocess.Popen(['xclip', '-selection', 'c'], stdin=subprocess.PIPE)
        p.communicate(input=text.encode('utf-8'))
    elif sys.platform == "win32":
        # Windows
        pyperclip.copy(text)
    else:
        st.error("Clipboard support is not available for this OS.")


def spacer(height: int = 30):
    """Used to align widgets horizontally."""
    return st.write(f'<div style="height: {height}px;"></div>', unsafe_allow_html=True)
