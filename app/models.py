from database import Base
from domain.enums import ItemType, Rarity, Status
from sqlalchemy import Column, Integer, String, DateTime, Enum as SAEnum
from sqlalchemy.sql import func


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    item_type = Column(SAEnum(ItemType), nullable=False)
    rarity = Column(SAEnum(Rarity), nullable=False)
    power = Column(Integer)
    status = Column(SAEnum(Status), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    time_required = Column(Integer)
