# Smart Home Project

This is a smart home project with a web application interface (frontend and backend) and an Arduino system integration. The backend is powered by Django, while the frontend is built using HTML, CSS, and JavaScript.

## Table of Contents
- [Project Structure](#project-structure)
- [How to Clone the Repository](#how-to-clone-the-repository)
- [Backend Setup](#backend-setup)
  - [Install Libraries](#install-libraries)
  - [Run the Backend](#run-the-backend)
- [Frontend](#frontend)
- [Arduino](#arduino)

---

## Project Structure

plaintext
smart-home-project/
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── script.js
├── backend/
│   ├── manage.py
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── requirements.txt
│   ├── venv/
├── arduino/
│   ├── main.ino
├── README.md


# How to Clone and Run the Smart Home Project

## Clone the Repository
To set up the project on your local machine, follow these steps:

1. Open your terminal.
2. Navigate to the directory where you want to clone the project.
3. Clone the repository and move into the project directory:

   ```bash
   git clone https://github.com/javohuz/smart_house.git
   cd smart-house-project


## Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd backend
Create a Python virtual environment to manage dependencies:

bash
Copy code
python3 -m venv venv
Activate the virtual environment:

For Linux/MacOS:

bash
Copy code
source venv/bin/activate
For Windows:

bash
Copy code
venv\Scripts\activate
Install the required Python libraries listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
Apply database migrations to prepare the database:

bash
Copy code
python manage.py migrate
Start the Django development server:

bash
Copy code
python manage.py runserver

The server will be accessible at http://127.0.0.1:8000.