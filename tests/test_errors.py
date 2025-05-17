import unittest
from app import create_app, db
from app.config import TestingConfig


class ErrorHandlersTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_404_not_found(self):
        res = self.client.get("/nonexistent-endpoint")
        data = res.get_json()
        self.assertEqual(res.status_code, 404)

        self.assertFalse(data["success"])
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"].lower(), "resource not found")

    def test_400_bad_request(self):
        # POST /actors with invalid (empty) payload
        res = self.client.post("/actors/", json={})
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data["success"])
        self.assertEqual(data["error"], 400)
        self.assertEqual(data["message"].lower(), "bad request")

    def test_422_unprocessable(self):
        # Simulate by POSTing to /actors with missing required fields
        payload = {"name": "Missing Age", "gender": "female"}  # age is required
        res = self.client.post("/actors/", json=payload)
        data = res.get_json()

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data["success"])
        self.assertEqual(data["error"], 422)
        self.assertEqual(data["message"].lower(), "unprocessable entity")

    def test_401_unauthorized(self):
        # Simulate 401 by manually aborting in a custom test route
        @self.app.route("/unauthorized-test")
        def unauthorized_test():
            from flask import abort
            abort(401)

        res = self.client.get("/unauthorized-test")
        data = res.get_json()

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])
        self.assertEqual(data["error"], 401)
        self.assertEqual(data["message"].lower(), "unauthorized")


if __name__ == "__main__":
    unittest.main()
