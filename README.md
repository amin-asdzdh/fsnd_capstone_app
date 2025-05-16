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
