import unittest
from datetime import datetime
from app import create_app, db
from app.models import Movie
from app.config import TestingConfig


class MoviesTestCase(unittest.TestCase):
    def setUp(self):
        """Create a test app and use in-memory SQLite."""
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        """Clean up after each test."""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_movies(self):
        """Test GET /movies returns a list."""

        with self.app.app_context():
            movie = Movie(title="Inception", release_date=datetime(2010, 7, 16))
            db.session.add(movie)
            db.session.commit()

        res = self.client.get("/movies/")
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertGreaterEqual(len(data["movies"]), 1)
        self.assertEqual(data["movies"][0]["title"], "Inception")


if __name__ == "__main__":
    unittest.main()
