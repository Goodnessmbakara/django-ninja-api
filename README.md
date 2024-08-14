# Django Ninja Inventory API

This project is a simple inventory management API built using Django Ninja. The API allows users to manage categories and products within the inventory. Additionally, the project includes basic user authentication (register, login, and logout) and CSRF token generation.

## Features

- **Category Management**
  - Create, Update, Retrieve, and Delete categories.
  
- **Product Management**
  - Create products and assign them to categories.
  - Retrieve products by category.
  
- **User Authentication**
  - Register new users.
  - Login and Logout functionality with Django's built-in authentication system.
  
- **CSRF Token Management**
  - Generate CSRF tokens for security.

## Requirements

- Python 3.8+
- Django 4.0+
- Django Ninja 0.13.0+
- Ninja JWT
- Other dependencies specified in `requirements.txt`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Goodnessmbakara/django-ninja-api.git
cd django-ninja-api
```

2. Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

## API Endpoints

### Category Management

- **Create Category**

  ```http
  POST /api/inventory/category
  ```

  Request body:

  ```json
  {
    "name": "Category Name",
    "slug": "category-name"
  }
  ```

- **Get All Categories**

  ```http
  GET /api/inventory/category/all
  ```

- **Update Category**

  ```http
  PUT /api/inventory/category/{category_id}
  ```

  Request body:

  ```json
  {
    "name": "Updated Name",
    "slug": "updated-name"
  }
  ```

- **Delete Category**

  ```http
  DELETE /api/inventory/category/{cat_id}
  ```

### Product Management

- **Create Product**

  ```http
  POST /api/inventory/product
  ```

  Request body:

  ```json
  {
    "name": "Product Name",
    "web_id": "unique-id",
    "category_id": 1
  }
  ```

- **Get Products by Category**

  ```http
  GET /api/inventory/product/category/{category_slug}
  ```

### User Authentication

- **Register User**

  ```http
  POST /api/register
  ```

  Request body:

  ```json
  {
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```

- **Login User**

  ```http
  POST /api/login
  ```

  Request body:

  ```json
  {
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```

- **Logout User**

  ```http
  POST /api/logout
  ```

### CSRF Token

- **Get CSRF Token**

  ```http
  GET /api/set-csrf-token
  ```

## Testing

To run the tests, use the following command:

```bash
python manage.py test
```

## Models

### `Category`

- `name`: The name of the category.
- `slug`: The slug used for URL routing.

### `Product`

- `name`: The name of the product.
- `web_id`: A unique identifier for the product.
- `category`: A foreign key linking the product to a category.

### User Model

A custom user model is utilized with email as the unique identifier for authentication.

## Schema

### `CategorySchema`

Used for handling category-related operations.

```python
class CategorySchema(Schema):
    name: str
    slug: str
```

### `ProductSchema`

Used for handling product-related operations.

```python
class ProductSchema(ModelSchema):
    class Config:
        model = Product
        model_fields = ["name", "web_id", "category"]
```

### `SignInSchema`

Used for user login and registration.

```python
class SignInSchema(BaseModel):
    email: str
    password: str
```

## Project Structure

```plaintext
.
├── api/
│   ├── __init__.py
│   ├── api.py
│   ├── schemas.py
│   └── urls.py
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── inventory/
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── README.md
```
