import json
import os
import bcrypt

# Path to the users.json file (assumes data/ folder is in the project root)
USERS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "users.json")

def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))

def signup(username, password, full_name):
    users = load_users()
    if username in users:
        return False, "Username already exists."
    users[username] = {"name": full_name, "password": hash_password(password)}
    save_users(users)
    return True, "User signed up successfully."

def login(username, password):
    users = load_users()
    if username in users and verify_password(password, users[username]["password"]):
        return True, users[username]["name"]
    return False, "Invalid username or password."
