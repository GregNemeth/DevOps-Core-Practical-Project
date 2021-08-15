from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase
from service_4.application import app, db
from service_4.application.models import History, Nexus



class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///utest.db"
        )
        return app

    def setUp(self):
        db.drop_all()
        db.create_all()

        filler = [
                (1,'It is certain'),
                (2,'Very doubtful'),
                (3,'It is decidedly so'),
                (4,'My reply is no'),
                (6,'Yes definitely'),
                (8, 'Reply hazy, try again'),
                (9,'The gods are with you on this one'),
                (12,'Ask again later'),
                (10,'To truly find yourself, you should play hide and seek alone'),
                (20,'Pass the bill to the person on your left'),
                (30,'When in anger, sing the alphabet'),
                (40,'The fortune you seek is in another cookie'),
                (60,'Dont panic'),
                (80, 'ERROR 404. fortune not found'),
                (90,'Ooops. Wrong cookie'),
                (120,'You are not illiterate')
                  ]

        for entry in filler:
            db.session.add(Nexus(id=entry[0], omen=entry[1]))
        db.session.commit()

        history_filler = [
                (1, 1, 'It is certain'),
                (1, 2,'Very doubtful'),
                (1, 3,'It is decidedly so'),
                (2, 2,'My reply is no'),
                (2, 3,'Yes definitely'),
                (4, 2, 'Reply hazy try again'),
                (3, 3,'The gods are with you on this one'),
                (4, 3,'Ask again later')
        ]

        for item in history_filler:
            db.session.add(History(a=item[0],b=item[1],x=(item[0]*item[1]),res=item[2]))
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        

class TestCreate(TestBase):
    def test_service_4(self):
        omens = [
                'It is certain',
                'Very doubtful',
                'It is decidedly so',
                'My reply is no',
                'Yes definitely',
                'Reply hazy try again',
                'The gods are with you on this one',
                'Ask again later',
                'To truly find yourself, you should play hide and seek alone',
                'Pass the bill to the person on your left',
                'When in anger, sing the alphabet',
                'The fortune you seek is in another cookie',
                'Dont panic',
                'ERROR 404. fortune not found',
                'Ooops. Wrong cookie',
                'You are not illiterate'
                  ]

        for i in range(1, 5):
            for j in range(1,4):

                response = self.client.post(
                    url_for('service_4'),
                    json={
                        'a': i,
                        'b': j
                        },
                    follow_redirects=True
                    )

        self.assertIn(response.json['m'], range(1, 121))
        self.assertIn(response.json['prophecy'], omens)
        for x in range(0, 5):
            self.assertIn(response.json['last_5'][x], omens)
        self.assert200(response)
