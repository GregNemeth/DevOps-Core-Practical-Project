from application.models import Nexus, History
from application import db

db.create_all()

db.session.add(History(id=1,a=2,b=3,x=6,res='Yes definitely'))
populate = [
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

for list in populate:
    try:
        item = Nexus(id=list[0],omen=list[1])
        db.session.add(item)
    except Exception: pass 
        

db.session.commit()
