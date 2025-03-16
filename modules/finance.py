import streamlit as st
import json
import os
import pandas as pd
import plotly.express as px

def get_finance_file(username):
    # Ensure the data directory exists
    file_path = os.path.join("data", f"finance_{username}.json")
    return file_path

def load_finance(username):
    file_path = get_finance_file(username)
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_finance(username, data):
    file_path = get_finance_file(username)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(username, category, amount, date, description):
    data = load_finance(username)
    expense = {
        "category": category,
        "amount": float(amount),
        "date": str(date),
        "description": description
    }
    data.append(expense)
    save_finance(username, data)

def display_dashboard():
    username = st.session_state.logged_in_user
    st.header("Finance Manager")
    with st.expander("Add Expense"):
        with st.form("add_expense_form"):
            category = st.text_input("Category", value="General")
            amount = st.number_input("Amount", min_value=0.0, format="%.2f")
            date = st.date_input("Date")
            description = st.text_area("Description")
            if st.form_submit_button("Add Expense"):
                add_expense(username, category, amount, date, description)
                st.success("Expense added successfully!")
    st.subheader("Expenses")
    data = load_finance(username)
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
        summary = df.groupby("category")["amount"].sum().reset_index()
        fig = px.bar(summary, x="category", y="amount", title="Expenses by Category")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No expenses recorded yet.")
