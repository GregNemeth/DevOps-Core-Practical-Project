from application.models import Nexus, History
from application import db

db.drop_all()
db.create_all()

db.session.add(History(id=1,a=2,b=3,x=6))
populate = [
    (1,'It is certain'),(2,'Very doubtful'),(3,'It is decidedly so'),
(4,'My reply is no'),(5, 'Concentrate and ask again'),(6,'Yes definitely'),
(7, 'Reply hazy, try again'),(8,'The gods are with you on this one'),(9,'Ask again later')
    ]

for list in populate:
    item = Nexus(id=list[0],omen=list[1])
    db.session.add(item)

db.session.commit()
