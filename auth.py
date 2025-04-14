from streamlit_auth0 import login_button
import streamlit as st

def auth_login():
    user_info = login_button(
        client_id="UY3ZtEuNv7mraViLlnD5uW8sSQDKPtMr",
        domain="dev-kl2x2fjpqz88xkgk.us.auth0.com",
    )

    if user_info:
        st.session_state['user'] = user_info
        return True
    return False
