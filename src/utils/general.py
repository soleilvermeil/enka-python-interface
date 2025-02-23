import os
import requests
import json
from typing import Any, cast
import datetime as dt
import logging


AnyNumber = int | float


def nested_get(
    data: dict[Any, Any],
    *keys: Any,
    default: Any | None = None,
) -> Any:
    """
    Get a nested value from a dictionary. If the value is not found,
    None is returned instead.

    Args:
        data (dict): The dictionary to search in.
        keys (str): The keys to search for.
        default (Any, optional): The default value to return if the keys
            are not found. Defaults to None.

    Returns:
        Any: The value found in the dictionary.
    """
    current: dict | Any = data.copy()
    for key in keys:
        if key not in current:
            return default
        current = current[key]
    return current


def smart_json_load(
    url: str,
    folder: str | None = None,
    expiration: dt.timedelta | None = None,
) -> Any:
    """
    Load a file from a URL. If a cache folder is provided, the file is
    loaded and saved in the cache folder if possible. If none is
    provided, the file will always be loaded from the URL.

    Args:
        url (str): The URL to load the file from.
        folder (str, optional): The folder to cache the file in.
            Defaults to None.
        expiration (dt.timedelta, optional): The time after which the
            file is considered expired. If None, the file never expires.
            Defaults to None.

    Returns:
        Any: The content of the file.
    """
    # If cache folder provided, check if the file exist. If it does,return
    # its content.
    file_name: str
    file_path: str
    if folder is not None:

        # Check if file exists
        file_name = os.path.basename(url)
        file_path = os.path.join(folder, file_name)
        if os.path.isfile(file_path):

            # Get the last modification date of the file
            timestamp: float = os.path.getmtime(file_path)
            last_modification: dt.datetime = dt.datetime.fromtimestamp(timestamp)

            # Load data only if the file is not expired. If no expiration is
            # provided, the file does never expire (i.e. it is only loaded
            # once).
            if expiration is None or dt.datetime.now() - last_modification < expiration:
                logging.debug(f"Loading {file_name} from cache")
                with open(file_path, "r") as f:
                    return json.load(f)
            else:
                logging.debug(f"{file_name} is expired. Fetching from URL")

    # If no cache folder is provided or if the file does not exist, load the
    # file from the URL
    response = requests.get(url)
    response.raise_for_status()
    data = json.loads(response.text)

    # If cache folder provided (and thus we are allowed to use file caching),
    # save the file in the cache folder
    folder = cast(str , folder)
    os.makedirs(folder, exist_ok=True)
    if folder is not None:
        with open(file_path, "w") as f:
            json.dump(data, f)

    # Finally return the data
    return data


def map_range(x: AnyNumber, x1: AnyNumber, x2: AnyNumber, y1: AnyNumber, y2: AnyNumber) -> AnyNumber:
    """
    Map a value from one range to another.
    """
    return y1 + (x - x1) * (y2 - y1) / (x2 - x1)