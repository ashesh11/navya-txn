Project Setup:
    - install dependencies: pip install -r requirements.txt
    - create a psql database
    - create .env file in refrence to .env.example
    - run migrations: python manage.py migrate
    - create superuser: python manage.py createsuperuser
    - run server: python manage.py runserver

Account Creation:
    - use email-signup endpoint to create user
    - go to admin panel using superuser account to provide role to that user

Account login:
    - use proper credentials to login and get authentication token
    - add that token to Authentication header as 'Bearer <token>' and access the authorized endpoints

