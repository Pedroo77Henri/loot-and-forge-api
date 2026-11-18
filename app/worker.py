from time import sleep
from database import SessionLocal
from infrastructure.repositories.item_repository import SqlAlchemyItemRepository
from use_cases.finish_forge import FinishForge


def run_once():
    db = SessionLocal()
    try:
        repository = SqlAlchemyItemRepository(db)
        FinishForge(repository).execute()
    finally:
        db.close()


def run():
    while True:
        run_once()
        sleep(60)


if __name__ == "__main__":
    run()
