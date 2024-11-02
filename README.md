### Project Setup

1. **Install Dependencies**
    - Install all required packages using:
      ```bash
      pip install -r requirements.txt
      ```

2. **Create PostgreSQL Database**
    - Set up a new PostgreSQL database for the project.

3. **Configure Environment Variables**
    - Copy `.env.example` to `.env` and update it with the appropriate database credentials and secret key.

4. **Run Migrations**
    - Apply database migrations with:
      ```bash
      python manage.py migrate
      ```

5. **Create Superuser**
    - Create an admin account to access the Django admin panel:
      ```bash
      python manage.py createsuperuser
      ```

6. **Start the Server**
    - Launch the Django development server:
      ```bash
      python manage.py runserver
      ```

---

### Account Creation

1. **User Signup**
    - Register a new user by sending a POST request to the `/email-signup` endpoint with the required details.

2. **Assign Role**
    - Log in to the Django admin panel at `/admin` using the superuser account. Assign the appropriate role (Staff or Manager) to the new user.

---

### Account Login and Access

1. **Login to Obtain Token**
    - Use the `/login` endpoint with the user’s credentials (email and password) to receive an authentication token.

2. **Authorize Requests**
    - Include the token in the `Authorization` header as shown below to access protected endpoints:
      ```plaintext
      Authorization: Bearer <token>
      ```
