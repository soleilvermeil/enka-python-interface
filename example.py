from src.interface import Player, Character
from src.types import Stat


def main() -> None:

    # Create the player object
    player: Player = Player(uid=703047530)

    if len(player.characters) == 0:
        print("No characters found")
        return

    # Get a character and print their stats
    character: Character = player.characters[0]
    print(character.name)
    for s in Stat:
        print(f"{s}: {character.stats.get(s):.1f}")


if __name__ == "__main__":
    main()
