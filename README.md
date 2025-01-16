# Connectify

**Connectify** is a Django-based web application that serves as a link-in-bio tool, similar to Linktree. It allows users to create a personalized page with multiple links, which they can share with their followers. This project is built with Django and follows a simple and clean approach to provide users with an easy way to manage and share their online presence.

## Features

- **Customizable Profiles**: Personalize your profile page with a bio and profile picture to showcase your unique identity.
- **User Authentication**: Secure signup and login functionality to keep your account safe and protected.
- **Password Recovery**: Forgetten your password? No worries! Simply use the email you registered with to reset and regain access to your account.
- **CRUD Operations**: Add, update, delete, and manage your links effortlessly.
- Minimalist design and clean interface to provide an easy user experience.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, SCSS, JavaScript
- **Database**: SQLite (default), but you can switch to PostgreSQL or MySQL
  
## Getting Started

### Prerequisites

- Python 3.8+
- Django 3.x+
- pip

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/connectify.git
    cd connectify
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin panel:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and visit `http://127.0.0.1:8000/` to see the app in action.


## Contributing
- Fork the repository.
- Create your branch (`git checkout -b feature/your-feature`).
- Commit your changes (`git commit -am 'Add new feature`).
- Push to the branch (`git push origin feature/your-feature`).
- Open a pull request.
