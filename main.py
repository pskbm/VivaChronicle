import openai
import streamlit as st
import streamlit_authenticator as stauth
import streamlit_antd_components as sac
from modules.home import CONTENT
from modules.todo import ToDo


if 'myopenai_key' not in st.session_state:
    st.session_state.myopenai_key = ''


def clear_key_cb():
    st.session_state.myopenai_key = ''


def main():
    authenticator = stauth.Authenticate(
            dict(st.secrets['credentials']),
            st.secrets['cookie']['name'],
            st.secrets['cookie']['key'],
            st.secrets['cookie']['expiry_days'],
            st.secrets['preauthorized']
        )
    
    # Build sidebar menu using Antd.
    with st.sidebar:
        smenu = sac.menu(
            [
                sac.MenuItem('Home', icon='house-fill'),
                sac.MenuItem('Chat', icon='chat-dots-fill'),
                sac.MenuItem(
                    'Authentication',
                    icon='person-workspace',
                    children=[
                        sac.MenuItem('Login', icon='arrow-right-square-fill'),
                        sac.MenuItem('Logout', icon='lock-fill'),
                    ]
                ),
                sac.MenuItem(
                    'Apps',
                    icon='layout-wtf',
                    children=[
                        sac.MenuItem('Todo', icon='list-check'),
                        sac.MenuItem('Fitness', icon='person-arms-up'),
                    ]
                ),                
            ],
            open_all=True,
            key='menu_k'
        )

    if smenu == 'Home':
        st.header(smenu)

        if st.session_state.authentication_status:            
            st.markdown(CONTENT)
        else:
            st.warning('Log in first in Login.')

    elif smenu == 'Todo':
        st.header(smenu)        

        if st.session_state.authentication_status:
            st.markdown(f'''username: **{st.session_state.username}**''')
            st.markdown(
                '''Except for username column, others can be edited but table cannot be saved.
                This is only a demo to check that the username who logged in is the same as the
                username shown in this table.
                ''')

            todo = ToDo(st.session_state.username)
            st.data_editor(
                todo.get_todo(),
                column_config={
                    'due': st.column_config.DateColumn(format="YYYY-MM-DD"),
                    'username': st.column_config.TextColumn(disabled=True),
                    'category': st.column_config.SelectboxColumn(options=['personal', 'work', 'others']),
                },
                use_container_width=True,
                hide_index=True,
                key='data_editor_k'
            )

    elif smenu == 'Fitness':
        st.header(smenu)

        if st.session_state.authentication_status:
            st.markdown(f'''username: **{st.session_state.username}**''')

            st.error('Comming soon ...')

    elif smenu == 'Logout':
        st.header(smenu)
        if st.session_state.authentication_status:
            st.write(f'Username: **{st.session_state["username"]}**')
            authenticator.logout('Logout', 'main', key='unique_key')

    elif smenu == 'Login':
        st.header(smenu)

        name, authentication_status, username = authenticator.login('Login', 'main')

        if authentication_status:
            st.write(f'Name: **{st.session_state["name"]}**, Username: **{st.session_state["username"]}**')

        elif authentication_status is None:
            st.session_state.myopenai_key = ''
            st.error('Username/password is incorrect')

        else:
            st.session_state.myopenai_key = ''
            st.warning('Please enter your username and password')

    elif smenu == 'Chat':
        st.header('Chat')

        openai_model = 'gpt-3.5-turbo'

        if st.session_state.authentication_status:
            st.markdown(f'''username: **{st.session_state.username}**, openai model: **{openai_model}**''')

            st.sidebar.text_input(
                'Enter your openai key',
                value=st.session_state.myopenai_key,
                key='openai_k',
                type='password'
            )
            st.session_state.myopenai_key = st.session_state.openai_k
            openai.api_key = st.session_state.myopenai_key

            st.sidebar.button('Clear Key', on_click=clear_key_cb)

            if "openai_model" not in st.session_state:
                st.session_state["openai_model"] = openai_model

            if "messages" not in st.session_state:
                st.session_state.messages = []

            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if prompt := st.chat_input("What is up?"):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    full_response = ""
                    try:
                        response = openai.chat.completions.create(
                            model=st.session_state["openai_model"],
                            messages=st.session_state.messages,
                            stream=True,
                        )
                    except openai.APIConnectionError as err:
                        st.error('Please enter your openai key in the sidebar.')
                        st.stop()
                    except Exception as err:
                        st.error(f'unexpected error: {err}')
                        st.stop()
                    else:
                        for part in response:
                            full_response += (part.choices[0].delta.content or "")
                            message_placeholder.markdown(full_response + "▌")
                        message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})

        else:
            st.warning('Log in first in Login.')


if __name__ == '__main__':
    main()
