from sqlalchemy.orm import Session
from domain.entities.character import Character
from domain.repositories import CharacterRepository
from models import Character as CharacterModel


def _to_entity(model: CharacterModel) -> Character:
    return Character(
        id=model.id,
        name=model.name,
        power=model.power,
        status=model.status,
    )


def _copy_to_model(character: Character, model: CharacterModel) -> None:
    model.name = character.name
    model.power = character.power
    model.status = character.status


class SqlAlchemyCharacterRepository(CharacterRepository):

    def __init__(self, db: Session):
        self.db = db

    def save(self, character: Character) -> Character:
        model = self.db.get(CharacterModel, character.id) if character.id else None
        if model is None:
            model = CharacterModel()
            self.db.add(model)
        _copy_to_model(character, model)
        try:
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        self.db.refresh(model)
        return _to_entity(model)

    def get_by_id(self, character_id: int) -> Character | None:
        model = self.db.get(CharacterModel, character_id)
        if model is None:
            return None
        return _to_entity(model)

    def list_all(self) -> list[Character]:
        return [_to_entity(model) for model in self.db.query(CharacterModel).all()]
