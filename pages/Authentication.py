import streamlit as st
import streamlit_authenticator as stauth


authenticator = stauth.Authenticate(
            dict(st.secrets['credentials']),
            st.secrets['cookie']['name'],
            st.secrets['cookie']['key'],
            st.secrets['cookie']['expiry_days'],
            st.secrets['preauthorized']
        )
    
tab1, tab2, tab3 = st.tabs(['Login', 'Register', 'Logout'])

with tab1:
    authenticator.login('Login', 'main')

    if st.session_state["authentication_status"]:
        st.write(f'Username: {st.session_state.username}')

    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

    else:
        st.error('Username/password is incorrect')

with tab2:
    st.error('This is not supported yet.')
    try:
        if authenticator.register_user('Register user', preauthorization=False):
            pass  # st.success('User registered successfully')
    except Exception as e:
        st.error(e)

with tab3:
    if st.session_state["authentication_status"]:
        authenticator.logout('Logout', 'main', key='unique_key')
        st.markdown(f'''
            Username: **{st.session_state["username"]}**  
            Name: **{st.session_state["name"]}**
            ''')

