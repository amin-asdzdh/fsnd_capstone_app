import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """
    Base configuration with sensible defaults.
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    # Secret key for session management and CSRF protection
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")

class DevelopmentConfig(BaseConfig):
    """
    Configuration for local development.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/casting_agency_db")
    )

class TestingConfig(BaseConfig):
    """
    Configuration for running tests.
    Uses in-memory SQLite database by default.
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///:memory:")

class ProductionConfig(BaseConfig):
    """
    Configuration for production deployments.
    Reads the DATABASE_URL from the environment.
    """
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    DEBUG = False
    # Ensure SECRET_KEY is set in environment for production
    SECRET_KEY = os.getenv("SECRET_KEY")
