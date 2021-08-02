from flask_testing import TestCase
from  application import app

class TestBase(TestCase):
    def create_app(self):
        return app

  # def setUp(self):


  # def tearDown(self):
       
class TestViews(TestBase):

    def test_service-2(self):
        response = self.client.get(
            url_for('service-2')
        )
        self.assertEqual(response.status_code, 200)

class TestService(TestBase):
    
    def test_service(self):
        response = self.client.get(
            url_for('service-2')
        )
        options = (1,2,3)

        for i in range(0, 20):
            assert response.data.decode() in options 
        
