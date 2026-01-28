# Flask CRUD API

A simple RESTful CRUD API built with **Flask** and **SQLAlchemy**.  
This project demonstrates basic backend concepts like routing, HTTP methods, and database interactions.

## Features
- Create, read, and delete resources
- REST-style endpoints
- SQLite database
- Tested using Postman

## Endpoints
- `GET /drinks` – List all drinks  
- `POST /drinks` – Add a new drink  
- `GET /drinks/<id>` – Get a drink by ID  
- `DELETE /drinks/<id>` – Delete a drink  

## Setup
```bash
pip install -r requirements.txt
flask run
```

## Tech Stack

- Flask
- Flask-SQLAlchemy
- SQLite
