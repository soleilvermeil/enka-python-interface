import logging


# Custom modules
from .utils import nested_get
from .genshinutils import *
from .genshintypes import *


class Equipment:

    def __init__(self, equipment_dict: WeaponDict | ArtifactDict) -> None:

        # Set rarity
        self.rarity: int = nested_get(equipment_dict, "flat", "rankLevel")

        # Set icon
        self.icon: str = nested_get(equipment_dict, "flat", "icon")


class Weapon(Equipment):
    def __init__(self, weapon_dict: WeaponDict) -> None:

        # Initialize the parent class
        super().__init__(weapon_dict)

        # Set level
        self.level: int = nested_get(weapon_dict, "weapon", "level")

        # Set rank
        self.rank: int = nested_get(weapon_dict, "weapon", "promoteLevel")

        # Prompt the creation
        logging.debug(f"Weapon created")


class Artifact(Equipment):
    def __init__(self, artifact_dict: ArtifactDict) -> None:

        # Initialize the parent class
        super().__init__(artifact_dict)

        # Set level
        self.level: int = get_artifact_level(artifact_dict)

        # Set rolls
        self.rolls: list[tuple[StatModifier, float]] = get_artifact_rolls(artifact_dict)

        # Set main stat
        self.main_stat: tuple[StatModifier, float] = get_artifact_main_stat(artifact_dict)

        # Set substats
        self.substats: list[tuple[StatModifier, float]] = get_artifact_substats(artifact_dict)

        # Prompt the creation
        logging.debug(f"Artifact created")


class Character:
    def __init__(self, character_dict: CharacterDict) -> None:

        # Set name
        self.name: str = get_character_name(character_dict)

        # Set level
        self.level: int = 1  # TODO

        # Set stats
        self.stats: dict[Stat, float] = {s: get_character_stat(character_dict, s) for s in Stat}

        # Set constellation
        self.constellation: int = 0  # TODO

        # Set weapon
        self.weapon: Weapon = Weapon(get_character_weapon(character_dict))

        # Set artifacts
        self.artifacts: dict[ArtifactType, Artifact | None] = {t: None for t in ArtifactType}
        for t in ArtifactType:
            artifact_dict: ArtifactDict | None = get_character_artifact(character_dict, t)
            if artifact_dict is not None:
                self.artifacts[t] = Artifact(artifact_dict)

        # Prompt the creation
        logging.debug(f"Character {self.name} created")


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"


class Player:
    def __init__(self, uid: int) -> None:

        # Get the player data
        player_dict: PlayerDict = get_player_dict(uid=uid)

        # Set nickname
        self.nickname: str = get_player_nickname(player_dict)

        # Set characters
        character_dicts: CharacterDict = nested_get(player_dict, "avatarInfoList")
        self.characters: list[Character] = [Character(character_dict) for character_dict in character_dicts]

        # Prompt the creation
        logging.debug(f"Player {self.nickname} created")


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.nickname})"
