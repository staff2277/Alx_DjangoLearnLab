# Advanced API Project with Django REST Framework

## Overview

This project implements a Django REST API with custom serializers, generic views, and authentication.

## API Endpoints

| Method | Endpoint                | Description            | Auth Required |
| ------ | ----------------------- | ---------------------- | ------------- |
| GET    | /books/                 | List all books         | No            |
| GET    | /books/<int:pk>/        | Retrieve a single book | No            |
| POST   | /books/create/          | Add a new book         | Yes           |
| PUT    | /books/update/<int:pk>/ | Update a book          | Yes           |
| DELETE | /books/delete/<int:pk>/ | Delete a book          | Yes           |

## Authentication

- Authenticated users can create, update, and delete books.
- Unauthenticated users can only read books.
- Authentication is handled via Django's Token Authentication.

## Running the Project

```sh
python manage.py runserver
```
