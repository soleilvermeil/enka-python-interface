from typing import Any
from enum import Enum


PlayerDict = dict[Any, Any]
CharacterDict = dict[Any, Any]
EquipmentDict = dict[Any, Any]
ArtifactDict = dict[Any, Any]
SubstatDict = dict[Any, Any]
WeaponDict = dict[Any, Any]


class Stat(Enum):
    HP = "HP"
    ATK = "ATK"
    DEF = "DEF"
    CR = "Crit RATE"
    CD = "Crit DMG"
    ER = "Energy recharge"
    EM = "Elemental mastery"


class StatModifier(Enum):
    HP_FLAT = "HP"
    HP_PERCENT = "HP%"
    ATK_FLAT = "ATK"
    ATK_PERCENT = "ATK%"
    DEF_FLAT = "DEF"
    DEF_PERCENT = "DEF%"
    CR = "Crit RATE"
    CD = "Crit DMG"
    ER = "Energy recharge"
    EM = "Elemental mastery"
    HealingBonus = "Healing bonus"
    DMG_Physical = "Physical DMG bonus"
    DMG_Fire = "Fire DMG bonus"
    DMG_Electro = "Electro DMG bonus"
    DMG_Hydro = "Hydro DMG bonus"
    DMG_Anemo = "Anemo DMG bonus"
    DMG_Cryo = "Cryo DMG bonus"
    DMG_Geo = "Geo DMG bonus"
    DMG_Dendro = "Dendro DMG bonus"


class ArtifactType(Enum):
    FLOWER = "Flower of Life"
    PLUME = "Plume of Death"
    SANDS = "Sands of Eon"
    GOBLET = "Goblet of Eonothem"
    CIRCLET = "Circlet of Logos"


PERCENT_STAT_MODIFIERS: set[StatModifier] = {
    StatModifier.HP_PERCENT,
    StatModifier.ATK_PERCENT,
    StatModifier.DEF_PERCENT,
    StatModifier.CR,
    StatModifier.CD,
}
