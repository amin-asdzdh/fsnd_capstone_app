## Casting Agency App

### Project Motivation
The Casting Agency project simulates a company that produces films and manages the actors cast in them. As the Executive Producer, you need a streamlined system for creating movies, assigning actors, and controlling access to each action.

## Getting Started

### Initial Setup
Create a virtual environment and install all requirements
```
python3 -m venv .venv_casting_agency
source .venv_casting_agency/bin/activate

pip install -r requirements.txt
```

### Database Setup

```
# create a database
createdb casting_agency_db

# Initialise flask-migrate
flask db init
flask db migrate -m "Initial schema"
```

To apply migrations to the database
```
flask db upgrade
```

To generate new migration script
```
flask db migrate -m "Describe your change"
flask db upgrade
```

To roll back migrations
```
# to the most recent migration
flask db downgrade

# to a specific version
flask db downgrade <revision_hash>
```

You can get some dummy data loaded to the database using the psql file in the repo
```
createdb casting_agency_db
psql casting_agency_db < casting_agency_db.psql
```

## Running Tests
To run tests
```
python -m unittest discover -s tests
```


# DATA MODELING
# TODO build Flask endpoints following REST principles (GET, POST, PATCH, DELETE)
# TODO implement at least 2 GET, 1 POST, 1 PATCH, 1 DELETE routes
# TODO add @app.errorhandler handlers for 400, 401, 404, 422 errors with JSON responses

# API ARCHITECTURE
# TODO build Flask endpoints following REST principles (GET, POST, PATCH, DELETE)
# TODO implement at least 2 GET, 1 POST, 1 PATCH, 1 DELETE routes
# TODO add @app.errorhandler handlers for 400, 401, 404, 422 errors with JSON responses

# AUTHENTICATION / RBAC
# TODO configure Auth0 application (Domain, Client ID, API audience)
# TODO create at least 2 roles in Auth0 with distinct permissions
# TODO implement @requires_auth(permission) decorator:
#   - extract token from header
#   - decode/verify JWT
#   - check permissions and error if invalid/expired

# TESTING
# TODO write unittest cases for each endpoint:
#   - test success case
#   - test failure case
# TODO test at least 2 role-based access control scenarios per role

# DEPLOYMENT
# TODO deploy Flask app to Heroku/Render
# TODO set Auth0 config in deployment environment (.env or startup script)
# TODO document live API URL and Auth0 setup steps in README

# CODE QUALITY AND DOCUMENTATION
# TODO ensure all code follows PEP8 (flake8 or black)
# TODO name variables/functions clearly and consistently
# TODO add inline comments where logic is non-obvious
# TODO store secrets (Auth0 config, DB URL) as env vars
# TODO keep code DRY — avoid duplication
# TODO use consistent formatting and logical endpoint naming
# TODO verify app runs with no unhandled errors

# README CONTENT
# TODO write a project README including:
#   - Project motivation
#   - Hosted API base URL
#   - How to install dependencies
#   - How to run app locally
#   - Auth0 setup (reference setup.sh or .env)
#   - API endpoint documentation (routes, methods, sample responses)
#   - Defined RBAC permissions per role
