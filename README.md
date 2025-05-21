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

## Running the App
```
export FLASK_APP=app
export FLASK_ENV=development
flask run --reload
```

## Running Tests
To run tests
```
python -m unittest discover -s tests
```

# API Documentation
This project exposes RESTful endpoints for managing Actors and Movies.

### Actors API
GET /actors/
Returns a list of all actors.

Response:
```
{
  "success": true,
  "actors": [
    {
      "id": 1,
      "name": "John Doe",
      "age": 35,
      "gender": "male",
      "movies": [1, 2]
    },
    ...
  ]
}
```

POST /actors/
Creates a new actor.


Request Body (JSON):
```
{
  "name": "Jane Smith",
  "age": 28,
  "gender": "female"
}
```

Response:
```
{
  "success": true,
  "actor": {
    "id": 4,
    "name": "Jane Smith",
    "age": 28,
    "gender": "female",
    "movies": []
  }
}
```

Error Codes:
```
- 400 – Invalid or missing data
```

PATCH /actors/<int:actor_id>
Updates an existing actor’s attributes.

Request Body (JSON):
```
{
  "name": "Updated Name",
  "age": 40
}
```

Response:
```
{
  "success": true,
  "actor": {
    "id": 1,
    "name": "Updated Name",
    "age": 40,
    "gender": "male",
    "movies": [1]
  }
}
```

Error Codes:
```
- 404 – Actor not found
- 400 – Invalid payload
```

DELETE /actors/<int:actor_id>
Deletes an actor by ID.

Response:
```
{
  "success": true,
  "deleted": 1
}
```

Error Codes:
```
- 404 – Actor not found
- 500 – Deletion failed
```

## Movies API

GET /movies/
Returns a list of all movies.

Response:
```
{
  "success": true,
  "movies": [
    {
      "id": 1,
      "title": "Inception",
      "release_date": "2010-07-16T00:00:00",
      "actors": [
        {
          "id": 1,
          "name": "Leonardo DiCaprio",
          "age": 48,
          "gender": "male",
          "movies": [1]
        }
      ]
    },
    ...
  ]
}
```