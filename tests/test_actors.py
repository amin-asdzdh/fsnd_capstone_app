import unittest
from app import create_app, db
from app.models import Actor
from app.config import TestingConfig


class ActorsTestCase(unittest.TestCase):
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

    def test_get_actors(self):
        """Test GET /actors returns a list."""
        with self.app.app_context():
            db.session.add(Actor(name="Test", age=25, gender="female"))
            db.session.commit()

        res = self.client.get("/actors/")
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertGreaterEqual(len(data["actors"]), 1)

    def test_post_actor(self):
        """Test POST /actors creates a new actor."""
        payload = {"name": "Chad", "age": 30, "gender": "male"}
        res = self.client.post("/actors/", json=payload)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["actor"]["name"], "Chad")

    def test_delete_actor(self):
        """Test DELETE /actors/<id> deletes the actor."""

        with self.app.app_context():
            actor = Actor(name="To Delete", age=40, gender="male")
            db.session.add(actor)
            db.session.commit()
            actor_id = actor.id

            actors = Actor.query.all()
            self.assertEqual(len(actors), 1)

        res = self.client.delete(f"/actors/{actor_id}")
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["deleted"], actor_id)

        with self.app.app_context():
            self.assertIsNone(Actor.query.get(actor_id))


if __name__ == "__main__":
    unittest.main()
