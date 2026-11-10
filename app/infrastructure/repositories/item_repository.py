from sqlalchemy.orm import Session
from domain.entities.item import Item
from domain.enums import ItemType, Rarity
from domain.repositories import ItemRepository
from models import Item as ItemModel


def _to_entity(model: ItemModel) -> Item:
    return Item(
        id=model.id,
        name=model.name,
        item_type=model.item_type,
        rarity=model.rarity,
        power=model.power,
        status=model.status,
        created_at=model.created_at,
        time_required=model.time_required,
    )


def _copy_to_model(item: Item, model: ItemModel) -> None:
    model.name = item.name
    model.item_type = item.item_type
    model.rarity = item.rarity
    model.power = item.power
    model.status = item.status
    model.time_required = item.time_required


class SqlAlchemyItemRepository(ItemRepository):

    def __init__(self, db: Session):
        self.db = db

    def save(self, item: Item) -> Item:
        model = self.db.get(ItemModel, item.id) if item.id else None
        if model is None:
            model = ItemModel()
            self.db.add(model)
        _copy_to_model(item, model)
        try:
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        self.db.refresh(model)
        return _to_entity(model)

    def get_by_id(self, item_id: int) -> Item | None:
        model = self.db.get(ItemModel, item_id)
        if model is None:
            return None
        return _to_entity(model)

    def list_all(
        self,
        item_type: ItemType | None = None,
        rarity: Rarity | None = None,
        order_by: str | None = None,
        direction: str | None = None,
    ) -> list[Item]:
        query = self.db.query(ItemModel)
        if item_type:
            query = query.filter(ItemModel.item_type == item_type)
        if rarity:
            query = query.filter(ItemModel.rarity == rarity)

        columns = {"power": ItemModel.power, "created_at": ItemModel.created_at}
        column = columns.get(order_by)
        if column is not None:
            query = query.order_by(column.desc() if direction == "desc" else column.asc())

        return [_to_entity(model) for model in query.all()]

    def delete(self, item: Item) -> None:
        model = self.db.get(ItemModel, item.id)
        if model is None:
            return
        try:
            self.db.delete(model)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
