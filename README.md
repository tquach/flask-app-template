## Microservice Template using Flask

A Python3 web application template uses the following frameworks:

* Python3
* Flask
* SQLAlchemy

## Getting Started

Create a virtual environment and activate it.
```
$ python3 -m venv .virtualenv
$ . ./.virtualenv/bin/activate
```

Set the `FLASK_ENV` to `development
```
$ export FLASK_ENV=development
```

Install all dependencies.
```
$ pip install -r requirements.txt
```

Initialize the database.
```
$ flask init-db
```

Start the server in development mode:
```
$ flask run
```
