from fastapi import APIRouter, Depends
from pydantic import BaseModel
from dependencies import get_character_repository, get_item_repository
from domain.repositories import CharacterRepository, ItemRepository
from use_cases.create_character import CreateCharacter
from use_cases.equip_item import EquipItem
from use_cases.get_character import GetCharacter
from use_cases.list_characters import ListCharacters


router = APIRouter()


class CreateCharacterSchema(BaseModel):
    name: str
    power: int


@router.post("/personagens")
def create_character(
    info: CreateCharacterSchema,
    characters: CharacterRepository = Depends(get_character_repository),
):
    return CreateCharacter(characters).execute(name=info.name, power=info.power)


@router.get("/personagens")
def list_characters(characters: CharacterRepository = Depends(get_character_repository)):
    return ListCharacters(characters).execute()


@router.get("/personagens/{character_id}")
def get_character(
    character_id: int,
    characters: CharacterRepository = Depends(get_character_repository),
    items: ItemRepository = Depends(get_item_repository),
):
    return GetCharacter(characters, items).execute(character_id)


@router.post("/personagens/{character_id}/equipar/{item_id}")
def equip_item(
    character_id: int,
    item_id: int,
    characters: CharacterRepository = Depends(get_character_repository),
    items: ItemRepository = Depends(get_item_repository),
):
    return EquipItem(characters, items).execute(character_id, item_id)
