from flask_testing import TestCase
from  service_4.app import app
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app

class TestCreate(TestBase):
    def test_service_4(self):
        for i in range(1, 4):
            for j in range(1,4):

                response = self.client.post(
                    url_for('service_4'),
                    json={
                        'a': i,
                        'b': j
                        },
                    follow_redirects=True
                    )

        self.assertIn(response.json, range(1, 10))
        self.assert200(response)
