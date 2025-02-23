import os
from typing import Any
import json
import requests


# Custom modules
from ..constants.general import CONSTANTS_CACHE_FOLDER, CONSTANTS_CACHE_EXPIRATION
from ..utils.general import smart_json_load


# Set some constants
BASE_URL: str = "https://enka.network/api/uid"


# Load some other constants
CHARACTERS: dict[Any, Any] = smart_json_load(
    url="https://raw.githubusercontent.com/EnkaNetwork/API-docs/refs/heads/master/store/characters.json",
    folder=CONSTANTS_CACHE_FOLDER,
    expiration=CONSTANTS_CACHE_EXPIRATION,
)
LOC: dict[Any, Any] = smart_json_load(
    url="https://raw.githubusercontent.com/EnkaNetwork/API-docs/refs/heads/master/store/loc.json",
    folder=CONSTANTS_CACHE_FOLDER,
    expiration=CONSTANTS_CACHE_EXPIRATION,
)
RELIQUARIAFFIXEXCELCONFIGDATA: list[dict[str, Any]] = smart_json_load(
    url="https://gitlab.com/Dimbreath/AnimeGameData/-/raw/master/ExcelBinOutput/ReliquaryAffixExcelConfigData.json",
    folder=CONSTANTS_CACHE_FOLDER,
    expiration=CONSTANTS_CACHE_EXPIRATION,
)
