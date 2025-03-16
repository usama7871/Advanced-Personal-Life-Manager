import streamlit as st
from modules import auth, finance, health, goals, tasks

# Display a banner image (make sure assets/images/banner.jpg exists)
st.image("assets/images/banner.jpg", use_container_width=True)

# Initialize session state for authentication if not set.
if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None
    st.session_state.user_name = None

# ----------------------------
# Authentication Section
# ----------------------------
if st.session_state.logged_in_user is None:
    st.title("Sign In / Sign Up")
    auth_mode = st.radio("Select Option", ["Sign In", "Sign Up"])
    
    if auth_mode == "Sign Up":
        with st.form("signup_form"):
            full_name = st.text_input("Full Name")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            if st.form_submit_button("Sign Up"):
                if password != confirm_password:
                    st.error("Passwords do not match.")
                else:
                    success, message = auth.signup(username, password, full_name)
                    if success:
                        st.success(message)
                        st.session_state.logged_in_user = username
                        st.session_state.user_name = full_name
                    else:
                        st.error(message)
    else:  # Sign In
        with st.form("signin_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Sign In"):
                success, result = auth.login(username, password)
                if success:
                    st.success("Logged in successfully!")
                    st.session_state.logged_in_user = username
                    st.session_state.user_name = result
                else:
                    st.error(result)
    st.stop()

if st.sidebar.button("Logout"):
    st.session_state.logged_in_user = None
    st.session_state.user_name = None
    st.experimental_rerun()

# ----------------------------
# Main Application Navigation
# ----------------------------
st.title("Advanced Personal Life Manager")
st.write(f"Welcome, {st.session_state.user_name}!")

menu = st.sidebar.selectbox("Navigation", ["Dashboard", "Finance", "Health", "Goals", "Tasks"])

if menu == "Dashboard":
    st.header("Dashboard")
    st.subheader("Finance Overview")
    finance.display_dashboard()
    st.subheader("Health Overview")
    health.display_dashboard()
    st.subheader("Goals Overview")
    goals.display_dashboard()
    st.subheader("Tasks Overview")
    tasks.display_dashboard()
elif menu == "Finance":
    finance.display_dashboard()
elif menu == "Health":
    health.display_dashboard()
elif menu == "Goals":
    goals.display_dashboard()
elif menu == "Tasks":
    tasks.display_dashboard()
