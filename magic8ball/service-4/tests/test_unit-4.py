from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

  # def setUp(self):


  # def tearDown(self):


class TestViews(TestBase):
    
    def test_service-4(self):
        response = self.client.get(
            url_for('service-4')
            )
        self.assert200(response)

        
