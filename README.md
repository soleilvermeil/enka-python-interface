# Python Enka.Network interface

Python module acting as an interface with Enka.Network's API.

## Minimal example

The file `example.py` contains a minimal example of how to use the module.

```python
from src.interface import Player, Character
from src.types import Stat


def main() -> None:

    # Create the player object
    player: Player = Player(uid=703047530)

    # Get a character and print their stats
    character: Character = player.characters[0]
    print(character.name)
    for s in Stat:
        print(f"{s}: {character.stats.get(s):.1f}")


if __name__ == "__main__":
    main()
```
