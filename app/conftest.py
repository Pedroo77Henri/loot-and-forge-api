from database import Base
from routes import get_db
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

engine_teste = create_engine("sqlite:///./test.db")   # banco diferente
SessionLocal_teste = sessionmaker(bind=engine_teste)

Base.metadata.create_all(bind=engine_teste )


def get_db_teste():
    db = SessionLocal_teste()
    try:
        yield db
    finally:    
        db.close()

app.dependency_overrides[get_db] = get_db_teste 