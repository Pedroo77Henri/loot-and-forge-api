from enum import Enum


class ItemType(Enum):
    WEAPON = "Weapon"
    ARMOR = "Armor"
    POTION = "Potion"
    SCROLL = "Scroll"

class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"

class Status(Enum):
    READY = "Ready"
    FORGING = "Forging"
