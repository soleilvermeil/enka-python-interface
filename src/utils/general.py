import os
import requests
import json
from typing import Any, cast, TypeVar


AnyNumber = TypeVar("AnyNumber", int, float)


def nested_get(data: dict[Any, Any], *keys: str) -> Any:
    """
    Get a nested value from a dictionary. If the value is not found, None is
    returned instead.
    """
    current: dict | Any = data.copy()
    for key in keys:
        if key not in current:
            return None
        current = current[key]
    return current


def smart_json_load(
    url: str,
    cache_folder: str | None = None,
) -> Any:
    """
    Load a file from a URL. If a cache folder is provided, the file is loaded
    and saved in the cache folder if possible. If none is provided, the file
    will always be loaded from the URL.
    """
    # If cache folder provided, check if the file exist. If it does, return
    # its content.
    file_name: str
    file_path: str
    if cache_folder is not None:
        file_name = os.path.basename(url)
        file_path = os.path.join(cache_folder, file_name)
        if os.path.isfile(file_path):
            with open(file_path, "r") as f:
                return json.load(f)

    # If no cache folder is provided or if the file does not exist, load the
    # file from the URL
    response = requests.get(url)
    response.raise_for_status()
    data = json.loads(response.text)

    # If cache folder provided (and thus we are allowed to use file caching),
    # save the file in the cache folder
    cache_folder = cast(str , cache_folder)
    os.makedirs(cache_folder, exist_ok=True)
    if cache_folder is not None:
        with open(file_path, "w") as f:
            json.dump(data, f)

    # Finally return the data
    return data


def map_range(x: AnyNumber, x1: AnyNumber, x2: AnyNumber, y1: AnyNumber, y2: AnyNumber) -> AnyNumber:
    """
    Map a value from one range to another.
    """
    return y1 + (x - x1) * (y2 - y1) / (x2 - x1)