from flask_testing import TestCase
from app import app
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app

  # def setUp(self):


  # def tearDown(self):
       
class TestViews(TestBase):
    def test_service_2(self):
        response = self.client.get(
            url_for('service_2')
        )
        self.assertEqual(response.status_code, 200)

class TestService(TestBase):    
    def test_service(self):
        response = self.client.get(
            url_for('service_2')
        )
        options = (1,2,3,4)

        for i in range(0, 20):
            assert response.json in options 
        

        
