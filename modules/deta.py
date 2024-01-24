"""Manages Deta space drive.

Saves config.yaml in Deta drive.
"""


import yaml
import io

import streamlit as st
from yaml.loader import SafeLoader
from deta import Deta


DRIVE_NAME = st.secrets['DETA_DRIVE_NAME']
CONFIG_FN = 'config.yaml'


@st.cache_data
def init_deta_drive():
    drive = Deta(st.secrets['DATA_KEY'])
    return drive.Drive(DRIVE_NAME)


def dump_dict_to_yaml_stringio(config):
    """Dump the dictionary to a YAML format string"""
    yaml_str = yaml.dump(config)
    return io.StringIO(yaml_str)


def get_config_from_deta():
    """Get the config from Deta drive."""
    drive = init_deta_drive()
    response = drive.get(CONFIG_FN)
    content = response.read()
    return yaml.load(content, Loader=SafeLoader)


def save_config_to_deta(config):
    config_ref = dump_dict_to_yaml_stringio(config)
    drive = init_deta_drive()
    drive.put(CONFIG_FN, data=config_ref)
