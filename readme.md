# User API

A Flask application that performs CRUD operations on a MongoDB database for a User resource using a REST API

![Python Verson: 3.9.13](https://img.shields.io/badge/Python-3.9.13-green)

## Installation

Clone the project & change the directory to `user-api` root

```sh
git clone https://github.com/codeholmes/user-api.git
cd user-api/
```

Create a virtual environment in the project root & activate it

```sh
python3 -m venv .
source bin/activate
```

Install the dependencies in the virtual environment

```sh
pip3 install -r requirements.txt
```

## Run

Run the app use following code, it will start a `Flask` server:

```sh
python3 app.py
```

## Endpoints

| Endpoints            | Method Allowed |
| -------------------- | -------------- |
| `/users`             | `GET`          |
| `/users/<string:id>` | `GET`          |
| `/users`             | `POST`         |
| `/users/<string:id>` | `PUT`          |
| `/users/<string:id>` | `DELETE`       |
