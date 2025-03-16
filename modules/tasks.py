import streamlit as st
import json
import os
import pandas as pd
import plotly.express as px


def get_tasks_file(username):
    return os.path.join("data", f"tasks_{username}.json")

def load_tasks(username):
    file_path = get_tasks_file(username)
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(username, data):
    file_path = get_tasks_file(username)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def add_task(username, task, due_date):
    data = load_tasks(username)
    new_task = {
        "task": task,
        "due_date": str(due_date),
        "completed": False
    }
    data.append(new_task)
    save_tasks(username, data)

def mark_task_complete(username, index):
    data = load_tasks(username)
    if 0 <= index < len(data):
        data[index]["completed"] = True
        save_tasks(username, data)

def display_dashboard():
    username = st.session_state.logged_in_user
    st.title("Task Manager")
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Task Manager</h1>", unsafe_allow_html=True)

    with st.expander("Add New Task"):
        with st.form("add_task_form"):
            task = st.text_area("Task Description")
            due_date = st.date_input("Due Date")
            if st.form_submit_button("Add Task") and task:
                add_task(username, task, due_date)
                st.success("Task added successfully!")
    st.subheader("Your Tasks")
    col1, col2 = st.columns(2)
    with col1:
        st.button("Add Task", key="add_task_button", help="Click to add a new task")
    with col2:
        st.button("View Tasks", key="view_tasks_button", help="Click to view your tasks")

    data = load_tasks(username)
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
        task_index = st.number_input("Enter task index to mark as complete (0-based)", min_value=0, step=1)
        if st.button("Mark as Complete", key=f"complete_{task_index}"):

            mark_task_complete(username, int(task_index))
            st.success("Task marked as complete!")
    else:        
        # Create a bar chart for task completion rates
        completion_counts = df['completed'].value_counts()
        fig = px.bar(completion_counts, x=completion_counts.index, y=completion_counts.values,
                     labels={'x': 'Completion Status', 'y': 'Number of Tasks'},
                     title='Task Completion Rates')
        st.plotly_chart(fig)

        st.info("No tasks available.")
