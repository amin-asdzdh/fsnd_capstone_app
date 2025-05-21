## Casting Agency App

URL = https://casting-agency-bswr.onrender.com/

ASSISTANT_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FMFVzU2x4dENnTTJ5Y1U3ODE2cSJ9.eyJpc3MiOiJodHRwczovL2Rldi0wczV1djByMGdjbjEyOGJjLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2ODI5NTdiZDQ4MDg3ODAxZjM0YzYxNzIiLCJhdWQiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5IiwiaWF0IjoxNzQ3ODI1MzU0LCJleHAiOjE3NDc5MTE3NTQsImd0eSI6InBhc3N3b3JkIiwiYXpwIjoid0tLcExWY2ZBTmtmcHhXM3BENHd5TVE4a3c4d0NwZ2oiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.FBoriCwiaL3LGzg-E_ItnLoCi9QMQMX9R3ihaw8nldCDiZTT0q0BTFvieorTBOEfltOIogPFXPksgsT3zM-ZmFAeZ_RRcNwBLSeDIfIJ3Uj9aFQEyNKeulR_RlsDhmA78ktSOZtNe7B2NP386CtkhDra4Z4eoHLkSP-0M1kKryh_h2F0WBs3RnaySQQpwR423-70Nduf5FvblnE5IcagejELup0L5NgZGghpsUUOnx7s_OuYJ7rXs27_2r2OMR5yQBPa5gyGuiKSUz_nsdksdMYokn83EqMLl6cxbLUGhBsh-MzJD10_KuovfH2M60ns1xYIGzi4ZvC6DrZRHjSoAg"

DIRECTOR_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FMFVzU2x4dENnTTJ5Y1U3ODE2cSJ9.eyJpc3MiOiJodHRwczovL2Rldi0wczV1djByMGdjbjEyOGJjLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2ODI5NTg0YjQ4MDg3ODAxZjM0YzYxZDEiLCJhdWQiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5IiwiaWF0IjoxNzQ3ODI1NDc4LCJleHAiOjE3NDc5MTE4NzgsImd0eSI6InBhc3N3b3JkIiwiYXpwIjoid0tLcExWY2ZBTmtmcHhXM3BENHd5TVE4a3c4d0NwZ2oiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwb3N0OmFjdG9ycyJdfQ.pOyneRaJXj_ToJL_5bSdUj4WcNrCOW8XtNzIMnF5eptu1xtwnjajllZNUKqpNXO211GgFOVa1aaKKDOAOUgmTYIqAftCMKGQKpsZXbsoO7eHsmGVDem1pFXIKUcZfGkdsZgLPcWCFCtDX2fQy0Ix5L-8ApboBBEiRKFsHseeP4D6_r_KfZ_lYqcZ2Pw1WONpyVJrHAyvYL0lg_ApliMnpeLTMSCN5ujBcZZP60XqTVd3yBdc2FGgUgiFccDQ73Sr-eShn2v7bz_LLS4NbsnTTFvlaGpuvjzeXap07BgrTQ14Ts8gRohWQEociUyRNnrsU2hPx_MlwlRy0gtnMCFUKw"


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