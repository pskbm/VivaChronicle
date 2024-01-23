"""Manages Deta space drive integration."""


import yaml
import io

import streamlit as st
from yaml.loader import SafeLoader
from deta import Deta


DRIVE_NAME = 'viva_chronicle_drive'
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
