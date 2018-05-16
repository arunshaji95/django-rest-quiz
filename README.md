# Django REST Framework Quiz

A simple quiz application using Django-REST Framework

## Installation

Clone the repository using https/ssh
    ```git clone https://github.com/arunshaji95/django-rest-quiz.git```

Create a virtual environment
    ```
    virtualenv venv -p python3
    source venv/bin/activate
    ```

Install the required packages using
    ```
    pip install -r requirements.txt
    ```

Migrate
    ```python manage.py migrate```

Create a superuser
    ```python manage.py createsuperuser```

Run the development server
    ```python manage.py runserver```
    
Visit http://localhost:8000/admin. Login with superuser credentials. Add some categories, questions and choices. Create a quiz using the command -
    ```python manage.py prepare_random_quiz```

