import os
import unittest
from dotenv import load_dotenv

from app import create_app, db
from app.config import TestingConfig

load_dotenv(override=True)

ASSISTANT_TOKEN = os.getenv("ASSISTANT_TOKEN")
DIRECTOR_TOKEN = os.getenv("DIRECTOR_TOKEN")
INVALID_TOKEN = os.getenv("INVALID_TOKEN")


class RBACAuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.drop_all()
            db.create_all()

        self.new_actor = {
            "name": "RBAC Test Actor",
            "age": 30,
            "gender": "female"
        }

        self.new_movie = {
            "title": "RBAC Test Movie",
            "release_date": "2025-07-01"
        }

    # -------- CASTING ASSISTANT --------
    def test_assistant_can_view_actors(self):
        res = self.client.get("/actors/", headers={"Authorization": f"Bearer {ASSISTANT_TOKEN}"})
        self.assertEqual(res.status_code, 200)

    def test_assistant_cannot_add_actor(self):
        res = self.client.post("/actors/", json=self.new_actor, headers={"Authorization": f"Bearer {ASSISTANT_TOKEN}"})
        self.assertEqual(res.status_code, 403)

    def test_assistant_cannot_delete_actor(self):
        res = self.client.delete("/actors/1", headers={"Authorization": f"Bearer {ASSISTANT_TOKEN}"})
        self.assertEqual(res.status_code, 403)

    def test_assistant_can_view_movies(self):
        res = self.client.get("/movies/", headers={"Authorization": f"Bearer {ASSISTANT_TOKEN}"})
        self.assertEqual(res.status_code, 200)

    # -------- CASTING DIRECTOR --------
    def test_director_can_add_actor(self):
        res = self.client.post("/actors/", json=self.new_actor, headers={"Authorization": f"Bearer {DIRECTOR_TOKEN}"})
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn("actor", data)

    def test_director_can_patch_actor(self):
        # First create actor
        create_res = self.client.post("/actors/", json=self.new_actor, headers={"Authorization": f"Bearer {DIRECTOR_TOKEN}"})
        actor_id = create_res.get_json()["actor"]["id"]

        update_payload = {"age": 35}
        patch_res = self.client.patch(f"/actors/{actor_id}", json=update_payload, headers={"Authorization": f"Bearer {DIRECTOR_TOKEN}"})
        self.assertEqual(patch_res.status_code, 200)
        self.assertEqual(patch_res.get_json()["actor"]["age"], 35)

    def test_director_can_delete_actor(self):
        # Create actor to delete
        create_res = self.client.post("/actors/", json=self.new_actor, headers={"Authorization": f"Bearer {DIRECTOR_TOKEN}"})
        actor_id = create_res.get_json()["actor"]["id"]

        delete_res = self.client.delete(f"/actors/{actor_id}", headers={"Authorization": f"Bearer {DIRECTOR_TOKEN}"})
        self.assertEqual(delete_res.status_code, 200)
        self.assertEqual(delete_res.get_json()["deleted"], actor_id)

    def test_director_cannot_access_with_invalid_token(self):
        res = self.client.get("/actors/", headers={"Authorization": f"Bearer {INVALID_TOKEN}"})
        self.assertEqual(res.status_code, 403)


if __name__ == "__main__":
    unittest.main()
