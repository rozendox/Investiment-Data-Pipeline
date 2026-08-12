"""Download file module"""

import os
import requests


def download_file(url: str, folder_path: str) -> None:
    """Download a file from a URL and save it to a specified path."""
    os.makedirs(os.path.dirname(folder_path), exist_ok=True)
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    with open(folder_path, 'wb') as file:
        file.write(response.content)
