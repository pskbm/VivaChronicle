import streamlit as st
from modules.home import CONTENT
from modules.deta import CONFIG_FN, init_deta_drive


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
    # =========================================================================
    # Copy the local config file config.yaml to Deta space first.
    # Be sure the config.yaml and main app file location is the same.
    upload_local_config_to_deta = False
    if upload_local_config_to_deta:
        drive = init_deta_drive()
        fp = open(CONFIG_FN)
        drive.put(CONFIG_FN, data=fp)
        fp.close()
    # =========================================================================

    st.title('Home')
    st.markdown(CONTENT)


if __name__ == '__main__':
    main()
