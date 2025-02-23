import os
import datetime as dt


# Language when fetching data from the API
LANG: str = "en"


# Constants cache settings
CONSTANTS_CACHE_FOLDER: str = os.path.join("cache", "constants")
CONSTANTS_CACHE_EXPIRATION: dt.timedelta = dt.timedelta(days=1)


# Player cache settings
PLAYERS_CACHE_FOLDER: str = os.path.join("cache", "players")
PLAYER_CACHE_EXPIRATION: dt.timedelta = dt.timedelta(hours=1)
