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

# How to Clone and Run the Smart Home Project

## Clone the Repository
To set up the project on your local machine, follow these steps:

1. Open your terminal.
2. Navigate to the directory where you want to clone the project.
3. Clone the repository and move into the project directory:

   ```bash
   git clone https://github.com/javohuz/smart_house.git
   cd smart-house


## Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd backend
Create a Python virtual environment to manage dependencies:

2. Create a Python virtual environment to manage dependencies:

   ```bash
   python3 -m venv venv


3 Activate the virtual environment:

1. For Linux/MacOS:

    ```bash
    source venv/bin/activate
    
2. For Windows:

    ```bash
    venv\Scripts\activate

Installition

4. install the required Python libraries listed in requirements.txt

   ```bash
   pip install -r requirements.txt

5. Apply database migrations to prepare the database:

   ```bash
   python manage.py migrate

6. Start the Django development server:

   ```bash
   python manage.py runserver


The server will be accessible at http://127.0.0.1:8000.