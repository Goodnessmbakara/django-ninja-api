# Django-Ninja RESTful API

A RESTful API built with Django and Django-Ninja that allows users to create, read, update, and delete blog posts. The API includes JWT-based authentication, pagination, filtering, and unit tests.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Database Migration](#database-migration)
- [Creating a Superuser](#creating-a-superuser)
- [Running the Server](#running-the-server)
- [API Documentation](#api-documentation)
- [Authentication](#authentication)
  - [Obtain JWT Token](#obtain-jwt-token)
  - [Refresh JWT Token](#refresh-jwt-token)
- [API Endpoints](#api-endpoints)
  - [Blog Posts](#blog-posts)
    - [List Posts](#list-posts)
    - [Retrieve a Post](#retrieve-a-post)
    - [Create a Post](#create-a-post)
    - [Update a Post](#update-a-post)
    - [Delete a Post](#delete-a-post)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [License](#license)

---

## Features

- **CRUD Operations**: Create, Read, Update, and Delete blog posts.
- **JWT Authentication**: Secure the API using JSON Web Tokens.
- **Pagination**: Paginate the list of blog posts.
- **Filtering**: Filter blog posts by title.
- **Unit Tests**: Ensure the reliability of API endpoints.
- **API Documentation**: Interactive API docs available via Swagger UI.

## Prerequisites

- Python 3.8 or higher
- pip
- Git

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Goodnessmbakara/django-ninja-api.git
   cd django-ninja-api
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv .venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

   **Note**: If `requirements.txt` is not present, install the necessary packages:

   ```bash
   pip install django django-ninja djangorestframework djangorestframework-simplejwt
   ```

   Then, freeze the requirements:

   ```bash
   pip freeze > requirements.txt
   ```

## Environment Variables

For simplicity, this project uses Django's default settings. However, for production, it's recommended to use environment variables to manage sensitive information.

## Database Migration

Apply migrations to set up the SQLite database.

```bash
python manage.py migrate
```

## Creating a Superuser

Create a superuser to access the Django admin interface.

```bash
python manage.py createsuperuser
```

Follow the prompts to set the username, email, and password.

## Running the Server

Start the development server.

```bash
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/`.

## API Documentation

Django-Ninja provides interactive API documentation. Access it at:

- Swagger UI: [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)
- Redoc: [http://127.0.0.1:8000/api/redoc](http://127.0.0.1:8000/api/redoc)

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. Obtain a token to access protected endpoints.

### Obtain JWT Token

- **Endpoint**: `POST /api/auth/token/`

- **Request**:

  ```bash
  curl -X POST http://127.0.0.1:8000/api/auth/token/ \
       -H "Content-Type: application/json" \
       -d '{"username": "your_username", "password": "your_password"}'
  ```

- **Response**:

  ```json
  {
      "refresh": "your_refresh_token",
      "access": "your_access_token"
  }
  ```

  Save the `access` token to authenticate subsequent requests.

### Refresh JWT Token

- **Endpoint**: `POST /api/auth/token/refresh/`

- **Request**:

  ```bash
  curl -X POST http://127.0.0.1:8000/api/auth/token/refresh/ \
       -H "Content-Type: application/json" \
       -d '{"refresh": "your_refresh_token"}'
  ```

- **Response**:

  ```json
  {
      "access": "new_access_token"
  }
  ```

## API Endpoints

### Blog Posts

#### List Posts

- **Endpoint**: `GET /api/posts/`
- **Description**: Retrieve a list of blog posts with optional pagination and filtering.
- **Parameters**:
  - `title` (optional): Filter posts by title (case-insensitive).
  - `page` (optional): Page number (default: 1).
  - `per_page` (optional): Posts per page (default: 10).

- **Request**:

  ```bash
  curl -X GET "http://127.0.0.1:8000/api/posts/?title=django&page=1&per_page=5"
  ```

- **Response**:

  ```json
  [
      {
          "id": 1,
          "title": "Django Ninja Tutorial",
          "content": "Learn how to build APIs with Django Ninja.",
          "author_id": 1,
          "created_at": "2023-08-13T12:00:00Z",
          "updated_at": "2023-08-13T12:00:00Z"
      },
      ...
  ]
  ```

#### Retrieve a Post

- **Endpoint**: `GET /api/posts/{post_id}/`
- **Description**: Retrieve details of a specific post.

- **Request**:

  ```bash
  curl -X GET "http://127.0.0.1:8000/api/posts/1/"
  ```

- **Response**:

  ```json
  {
      "id": 1,
      "title": "Django Ninja Tutorial",
      "content": "Learn how to build APIs with Django Ninja.",
      "author_id": 1,
      "created_at": "2023-08-13T12:00:00Z",
      "updated_at": "2023-08-13T12:00:00Z"
  }
  ```

#### Create a Post

- **Endpoint**: `POST /api/posts/`
- **Description**: Create a new blog post. **Authentication required**.

- **Request**:

  ```bash
  curl -X POST "http://127.0.0.1:8000/api/posts/" \
       -H "Content-Type: application/json" \
       -H "Authorization: Bearer your_access_token" \
       -d '{
             "title": "New Post Title",
             "content": "Content of the new post."
           }'
  ```

- **Response**:

  ```json
  {
      "id": 2,
      "title": "New Post Title",
      "content": "Content of the new post.",
      "author_id": 1,
      "created_at": "2023-08-13T13:00:00Z",
      "updated_at": "2023-08-13T13:00:00Z"
  }
  ```

#### Update a Post

- **Endpoint**: `PUT /api/posts/{post_id}/`
- **Description**: Update an existing post. Only the author can update their posts. **Authentication required**.

- **Request**:

  ```bash
  curl -X PUT "http://127.0.0.1:8000/api/posts/2/" \
       -H "Content-Type: application/json" \
       -H "Authorization: Bearer your_access_token" \
       -d '{
             "title": "Updated Post Title",
             "content": "Updated content of the post."
           }'
  ```

- **Response**:

  ```json
  {
      "id": 2,
      "title": "Updated Post Title",
      "content": "Updated content of the post.",
      "author_id": 1,
      "created_at": "2023-08-13T13:00:00Z",
      "updated_at": "2023-08-13T14:00:00Z"
  }
  ```

#### Delete a Post

- **Endpoint**: `DELETE /api/posts/{post_id}/`
- **Description**: Delete an existing post. Only the author can delete their posts. **Authentication required**.

- **Request**:

  ```bash
  curl -X DELETE "http://127.0.0.1:8000/api/posts/2/" \
       -H "Authorization: Bearer your_access_token"
  ```

- **Response**:

  ```json
  {
      "success": true
  }
  ```

## Testing

Unit tests are written to ensure the reliability of API endpoints.

1. **Run Tests**

   ```bash
   python manage.py test
   ```

   This command will execute all tests in the `api/tests.py` file.

2. **Sample Output**

   ```bash
   Creating test database for alias 'default'...
   System check identified no issues (0 silenced).
   ....
   ----------------------------------------------------------------------
   Ran 4 tests in 0.512s

   OK
   Destroying test database for alias 'default'...
   ```

## Project Structure

```
django-ninja-api/
├── api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── schemas.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

## License

This project is licensed under the [MIT License](LICENSE).

# Contact

For any questions or suggestions, please contact [Your Name](mailto:your.email@example.com).

# Additional Notes

- For production deployment, consider using a more robust database like PostgreSQL.
- Always keep your secret keys and tokens secure.
- Enhance security by enabling HTTPS in production.

# Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Django-Ninja](https://django-ninja.rest-framework.com/)
- [Django REST Framework SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

# References

- [Django Documentation](https://docs.djangoproject.com/en/4.2/)
- [Django-Ninja Documentation](https://django-ninja.rest-framework.com/)
- [DRF SimpleJWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

---

*This README was generated as part of an interview task to demonstrate the implementation of a RESTful API using Django and Django-Ninja.*