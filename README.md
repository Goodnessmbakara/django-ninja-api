Here’s a comprehensive `README.md` for your Django-Ninja API project. This document is structured to cover all aspects of setting up, running, testing, and deploying your application in a production environment.

---

# Django-Ninja RESTful API

A RESTful API built with Django and Django-Ninja that allows users to create, read, update, and delete resources (e.g., blog posts). This project is designed with best practices in mind, including JWT-based authentication, pagination, filtering, unit tests, and production readiness with environment variable management using `python-dotenv` and static file handling using `whitenoise`.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Server](#running-the-server)
- [API Documentation](#api-documentation)
- [Authentication](#authentication)
- [Testing](#testing)
- [Deployment](#deployment)
- [Security Best Practices](#security-best-practices)
- [License](#license)

## Features

- **CRUD Operations**: Create, Read, Update, and Delete blog posts.
- **JWT Authentication**: Secure the API using JSON Web Tokens.
- **Pagination**: Paginate the list of blog posts.
- **Filtering**: Filter blog posts by title.
- **Unit Tests**: Ensure the reliability of API endpoints.
- **API Documentation**: Interactive API docs available via Swagger UI.
- **Production Ready**: Environment variable management with `python-dotenv` and static file handling with `whitenoise`.

## Prerequisites

- Python 3.8 or higher
- pip
- Git
- PostgreSQL (optional for production)

## Installation

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Goodnessmbakara/django-ninja-api.git
cd django-ninja-api
```

### 2. Create a Virtual Environment

Create and activate a virtual environment to isolate project dependencies.

```bash
python3 -m venv .venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages.

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root directory to manage your environment variables. Add the following variables:

```env
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3  # Update for production use
ALLOWED_HOSTS=127.0.0.1, .yourdomain.com
JWT_SECRET_KEY=your-jwt-secret-key
STATIC_ROOT=/path/to/staticfiles  # Update for production use
```

### 5. Apply Migrations

Run database migrations to set up your database.

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser

Create an admin user to access the Django admin interface.

```bash
python manage.py createsuperuser
```

## Running the Server

Start the development server to run the application locally.

```bash
python manage.py runserver
```

To serve the application in production, you'll need to configure a WSGI server (like Gunicorn) and a reverse proxy server (like Nginx). Refer to the [Deployment](#deployment) section below for more details.

## API Documentation

The API is documented using Swagger UI, which is automatically generated by Django-Ninja. To view the documentation, navigate to the following URL in your browser after running the server:

```
http://127.0.0.1:8000/api/docs
```

## Authentication

### Obtain JWT Token

To authenticate, you'll need to obtain a JWT token by providing your username and password:

```http
POST /api/auth/token/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

The response will include the access and refresh tokens:

```json
{
    "access": "your_access_token",
    "refresh": "your_refresh_token"
}
```

### Use JWT Token

Include the token in the `Authorization` header when making requests to protected endpoints:

```http
GET /api/posts/
Authorization: Bearer your_access_token
```

## Testing

Unit tests are provided to ensure the reliability of the API endpoints. To run the tests, execute the following command:

```bash
python manage.py test
```

This will run all the tests and output the results, helping you ensure the correctness and robustness of your API.

## Deployment

To deploy the application to a production environment, follow these steps:

### 1. Configure a Production Database

It is recommended to use a production-grade database like PostgreSQL. Update your `.env` file with the production database settings:

```env
DATABASE_URL=postgres://username:password@localhost:5432/dbname
```

### 2. Collect Static Files

Run the `collectstatic` command to gather all static files in the `STATIC_ROOT` directory:

```bash
python manage.py collectstatic
```

### 3. Use a WSGI Server

In production, use a WSGI server like Gunicorn to serve the application:

```bash
gunicorn django_ninja_api.wsgi:application --bind 0.0.0.0:8000
```


### 5. Security Hardening

- **Set Secure Headers**: Configure security headers like `Content-Security-Policy`, `X-Frame-Options`, and `X-Content-Type-Options`.
- **Use Environment Variables**: Never hard-code sensitive information like secret keys or database credentials in your code.

## Security Best Practices

- **Secret Management**: Use `python-dotenv` to manage environment variables securely.
- **Static Files Handling**: Use `whitenoise` to serve static files in production, ensuring they're compressed and cached efficiently.
- **CSRF Protection**: Ensured that the API is protected against Cross-Site Request Forgery (CSRF) attacks.
- **Rate Limiting**: Consider implementing rate limiting to protect the API against abuse.

## License

This project is licensed under the [MIT License](LICENSE).

---

This `README.md` provides comprehensive instructions and information, making the project easy to set up, run, test, and deploy while following best practices for security and production readiness. 