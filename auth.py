# from streamlit_auth0 import login_button
# import streamlit as st

# def auth_login():
#     user_info = login_button(
#         client_id="UY3ZtEuNv7mraViLlnD5uW8sSQDKPtMr",
#         domain="dev-kl2x2fjpqz88xkgk.us.auth0.com",
#     )

#     if user_info:
#         st.session_state['user'] = user_info
#         return True
#     return False

from streamlit_auth0 import login_button
import streamlit as st


def auth_login():
    st.markdown("""
    <div style="background-color:#fff8c4; padding:15px; border-radius:10px;">
        <h4 style="color:#665c00;">📸 Instructions</h4>
        <ul style="color:#665c00; font-size:16px;">
            <li>Upload high-quality eye images (jpg, jpeg, png).</li>
            <li>The system will predict the DR stage along with confidence levels.</li>
            <li>Results are displayed for each uploaded image.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


    user_info = login_button(
        client_id="UY3ZtEuNv7mraViLlnD5uW8sSQDKPtMr",
        domain="dev-kl2x2fjpqz88xkgk.us.auth0.com",
    )

    if user_info:
        st.session_state['user'] = user_info
        st.success(f"Login Successful! Welcome {user_info['name']} 👋")
        return True

    st.markdown("""
        <hr>
        <p style="text-align:center; color:gray;">Need Help? Contact Admin</p>
    """, unsafe_allow_html=True)

    return False
