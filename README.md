
# 🌟 Advanced Personal Life Manager

**Advanced Personal Life Manager** is an all-in-one, Streamlit-powered application designed to help you take charge of your personal life. Whether you're tracking finances, health, goals, or daily tasks—this interactive, modular platform has got you covered.

> Built with Python, Streamlit, Plotly, and modern UI practices—focused on productivity, personalization, and simplicity.

---

## 🔗 Table of Contents

- [✨ Features](#-features)
- [📁 Directory Structure](#-directory-structure)
- [⚙️ Installation](#️-installation)
- [🚀 Usage](#-usage)
- [☁️ Deployment](#-deployment)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## ✨ Features

### 🔐 User Authentication
- Secure sign-up/sign-in system using `bcrypt` password hashing.
- JSON-based user data storage per individual.

### 💰 Finance Management
- Log and categorize expenses.
- Visual insights with interactive bar charts for categories and trends.

### ❤️ Health Tracker
- Track health metrics: weight, sleep, etc.
- Line charts to monitor personal health trends over time.

### 🎯 Goal Setting
- Create, edit, and update life goals.
- Inline editing and goal completion status tracking.

### ✅ Task Manager
- Build personal to-do lists with deadlines and statuses.
- Direct in-app task editing with a clean layout.

### 📊 Dashboard & Data Viz
- Unified dashboard for Finance, Health, Goals, and Tasks.
- Real-time data visualization using Plotly.
- Custom CSS for a sleek, responsive UI.

---

## 📁 Directory Structure

```
advanced-personal-life-manager/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── config/
│   └── config.yaml
├── data/
│   └── users.json
├── modules/
│   ├── __init__.py
│   ├── auth.py
│   ├── finance.py
│   ├── health.py
│   ├── goals.py
│   └── tasks.py
└── assets/
    └── images/
        └── banner.jpg
```

---

## ⚙️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/usama7871/Advanced-Personal-Life-Manager.git
cd Advanced-Personal-Life-Manager
```

2. **Set Up Virtual Environment (Recommended)**

```bash
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on macOS/Linux
source venv/bin/activate
```

3. **Install Dependencies**

Ensure your `requirements.txt` includes the following:
```txt
streamlit
plotly
pandas
pyyaml
bcrypt
```

Then install:
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Start the app locally by running:

```bash
streamlit run app.py
```

Visit the provided localhost URL, log in or sign up, and begin managing your personal life seamlessly.

---

## ☁️ Deployment

### ▶️ Streamlit Cloud (Recommended)

1. Go to [Streamlit Cloud](https://share.streamlit.io/)
2. Click **"New App"** and link your GitHub repository.
3. Set `app.py` as the entry point.
4. Click **Deploy** and enjoy!

### ☁️ Heroku

1. Add a `Procfile` in the root directory:

```txt
web: streamlit run app.py --server.enableCORS false
```

2. Push to GitHub and connect it to your Heroku app for deployment.

---

## 🤝 Contributing

Contributions, ideas, and feedback are welcome!

- Fork the repo
- Create a new branch (`feature/your-feature`)
- Commit your changes
- Submit a Pull Request

For large contributions, please [open an issue](https://github.com/usama7871/Advanced-Personal-Life-Manager/issues) first.

---

## 📜 License

This project is licensed under the **[MIT License](LICENSE)**.

---

**Built for people who want to live intentionally, track their progress, and stay in control.**

**Manage your life. Visually. Efficiently. Intelligently.**

---

Happy coding!  
_— Usama_
