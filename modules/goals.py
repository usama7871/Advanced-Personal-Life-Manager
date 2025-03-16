import streamlit as st
import json
import os
import pandas as pd

def get_goals_file(username):
    return os.path.join("data", f"goals_{username}.json")

def load_goals(username):
    file_path = get_goals_file(username)
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_goals(username, data):
    file_path = get_goals_file(username)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def add_goal(username, description, due_date):
    data = load_goals(username)
    goal = {
        "description": description,
        "due_date": str(due_date),
        "completed": False
    }
    data.append(goal)
    save_goals(username, data)

def mark_goal_complete(username, index):
    data = load_goals(username)
    if 0 <= index < len(data):
        data[index]["completed"] = True
        save_goals(username, data)

def display_dashboard():
    username = st.session_state.logged_in_user
    st.header("Goals Manager")
    with st.expander("Add New Goal"):
        with st.form("add_goal_form"):
            description = st.text_area("Goal Description")
            due_date = st.date_input("Due Date")
            if st.form_submit_button("Add Goal") and description:
                add_goal(username, description, due_date)
                st.success("Goal added!")
    st.subheader("Your Goals")
    data = load_goals(username)
    if data:
        df = pd.DataFrame(data)
        edited_df = st.data_editor(df, num_rows="dynamic")

        if st.button("Save Changes"):
            save_goals(username, edited_df.to_dict(orient="records"))
            st.success("Goals updated!")
    else:
        st.info("No goals recorded yet.")
