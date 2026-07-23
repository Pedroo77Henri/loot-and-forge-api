from enum import Enum, auto
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum as SAEnum
from sqlalchemy.sql import func


class TipoItem(Enum):
    ARMA = auto()
    ARMADURA = auto()
    POCAO = auto()
    ACESSORIO = auto()

class Raridade(Enum):
    COMUM = "Comum"
    RARO = "Raro"
    EPICO = "Épico"
    LENDARIO = "Lendário"

class Status(Enum):
    PRONTO = 'Pronto'
    FORJANDO = 'Forjando'

class Item(Base):
    __tablename__ = "Itens"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    tipo = Column(SAEnum(TipoItem), nullable=False)
    raridade = Column(SAEnum(Raridade), nullable=False)
    poder = Column(Integer)
    status = Column(SAEnum(Status), nullable=False)
    criado_em = Column(DateTime, server_default=func.now())
    tempo_necessario = Column(Integer)