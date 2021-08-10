from flask_testing import TestCase
from service_3.app import app
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app

  # def setUp(self):


  # def tearDown(self):
       
class TestViews(TestBase):
    def test_service_3(self):
        response = self.client.get(
            url_for('service_3')
        )
        self.assertEqual(response.status_code, 200)

class TestService(TestBase):    
    def test_service(self):
        response = self.client.get(
            url_for('service_3')
        )
        options = (1,2,3)

        for i in range(0, 20):
            assert response.json in options 
        
