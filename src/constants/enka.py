import os
from typing import Any
import json
import requests


# Custom modules
from ..constants.general import CONSTANTS_CACHE_FOLDER
from ..utils.general import smart_json_load


# Set some constants
BASE_URL: str = "https://enka.network/api/uid"


# Load some other constants
CHARACTERS: dict[Any, Any] = smart_json_load(
    url="https://raw.githubusercontent.com/EnkaNetwork/API-docs/refs/heads/master/store/characters.json",
    cache_folder=CONSTANTS_CACHE_FOLDER,
)
LOC: dict[Any, Any] = smart_json_load(
    url="https://raw.githubusercontent.com/EnkaNetwork/API-docs/refs/heads/master/store/loc.json",
    cache_folder=CONSTANTS_CACHE_FOLDER,
)
RELIQUARIAFFIXEXCELCONFIGDATA: list[dict[str, Any]] = smart_json_load(
    url="https://gitlab.com/Dimbreath/AnimeGameData/-/raw/master/ExcelBinOutput/ReliquaryAffixExcelConfigData.json",
    cache_folder=CONSTANTS_CACHE_FOLDER,
)
