from database import SessionLocal
from models import Item, Status
from time import sleep
from random import randint
db = SessionLocal()
while True:
    query = db.query(Item).filter(Item.status == Status.FORGING).all()
    for item in query:
        time = item.time_required
        sleep(time)
        item.power = randint(80, 100)
        item.status = Status.READY
        db.commit()
    sleep(60)