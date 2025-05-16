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

# TODO define models
# TODO setup apis
# TODO setup tests
# TODO setup auth0 and permissions
