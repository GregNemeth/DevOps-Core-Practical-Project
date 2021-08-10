from flask_testing import TestCase
from flask import url_for
import requests_mock
from service_1.app import app


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_home(self):

        with requests_mock.mock() as m:

            m.get('http://service-2:5000/randnum', json=2)
            m.get('http://service-3:5000/randnum', json=3)
            m.post('http://service-4:5000/multiply',json={
                
                'last_5':[
                    'Very doubtful',
                    'It is decidedly so',
                    'My reply is no',
                    'Yes, definitely',
                    'Reply hazy try again',
                ], 'm': 6,
                'prophecy':'Yes, definitely'
            }
            )
            response = self.client.get('/')

        self.assert200(response)
        self.assertIn('Yes, definitely', response.data.decode())

