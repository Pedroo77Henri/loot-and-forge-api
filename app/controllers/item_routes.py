from fastapi import APIRouter, Depends
from pydantic import BaseModel
from dependencies import get_item_repository
from domain.enums import ItemType, Rarity
from domain.repositories import ItemRepository
from use_cases.create_item import CreateItem
from use_cases.delete_item import DeleteItem
from use_cases.forge_item import ForgeItem
from use_cases.get_item import GetItem
from use_cases.get_items import GetItems


router = APIRouter()


class CreateItemSchema(BaseModel):
    name: str
    item_type: ItemType
    rarity: Rarity
    power: int


class ForgeItemSchema(BaseModel):
    name: str
    time_required: int
    item_type: ItemType
    rarity: Rarity


@router.post("/itens")
def create_item(info: CreateItemSchema, repo: ItemRepository = Depends(get_item_repository)):
    return CreateItem(repo).execute(
        name=info.name,
        item_type=info.item_type,
        rarity=info.rarity,
        power=info.power,
    )


@router.post("/itens/forjar", status_code=202)
def forge_item(info: ForgeItemSchema, repo: ItemRepository = Depends(get_item_repository)):
    return ForgeItem(repo).execute(
        name=info.name,
        item_type=info.item_type,
        rarity=info.rarity,
        time_required=info.time_required,
    )


@router.get("/itens/{item_id}")
def get_item(item_id: int, repo: ItemRepository = Depends(get_item_repository)):
    return GetItem(repo).execute(item_id)


@router.get("/itens")
def get_items(
    item_type: ItemType | None = None,
    item_rarity: Rarity | None = None,
    order_by: str | None = None,
    direction: str | None = None,
    repo: ItemRepository = Depends(get_item_repository),
):
    return GetItems(repo).execute(item_type, item_rarity, order_by, direction)


@router.delete("/itens/{item_id}")
def delete_item(item_id: int, repo: ItemRepository = Depends(get_item_repository)):
    return DeleteItem(repo).execute(item_id)
