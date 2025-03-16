import streamlit as st
import json
import os
import pandas as pd
import plotly.express as px

def get_health_file(username):
    return os.path.join("data", f"health_{username}.json")

def load_health(username):
    file_path = get_health_file(username)
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_health(username, data):
    file_path = get_health_file(username)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def add_health_record(username, weight, sleep_hours, date, notes):
    data = load_health(username)
    record = {
        "weight": float(weight),
        "sleep_hours": float(sleep_hours),
        "date": str(date),
        "notes": notes
    }
    data.append(record)
    save_health(username, data)

def display_dashboard():
    username = st.session_state.logged_in_user
    st.header("Health Manager")
    with st.expander("Log Health Metrics"):
        with st.form("add_health_form"):
            weight = st.number_input("Weight (kg)", min_value=0.0, format="%.1f")
            sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, format="%.1f")
            date = st.date_input("Date")
            notes = st.text_area("Notes")
            if st.form_submit_button("Add Record"):
                add_health_record(username, weight, sleep_hours, date, notes)
                st.success("Health record added successfully!")
    st.subheader("Health Records")
    data = load_health(username)
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
        df["date"] = pd.to_datetime(df["date"])
        if "weight" in df.columns:
            fig = px.line(df, x="date", y="weight", title="Weight Over Time")
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No health records available.")
