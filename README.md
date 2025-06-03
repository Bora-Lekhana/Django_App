**🎉 Event Management System**

A Django-based web application for creating, managing, and attending events. Designed for organizers and participants to streamline event planning, registration, and communication.

**🚀 Features**
User authentication (Sign up, login, logout)

Event creation and editing (for organizers)

Event listing and search functionality

Registration system for attendees

Admin dashboard for event oversight

Email notifications for registration confirmations

Responsive design for all devices

**🛠 Tech Stack**
Backend: Django (Python)

Frontend: HTML, CSS, JavaScript, Bootstrap

Database: SQLite (default), with support for PostgreSQL

Authentication: Django's built-in authentication system

📦 Project Structure 
     This structure reflects a modular and scalable Django application design, separating configuration, core app logic, static resources, and templates for maintainability and clarity.
    
event_management/
├── event_management/        # Django project settings and configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── events/                  # Main app for handling events
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── static/                  # Static files (CSS, JS, images)
├── templates/               # Shared templates (base, login, etc.)
├── db.sqlite3               # Default database
├── manage.py                # Django CLI
└── README.md

![Event_Manaement](Event.jpg)
