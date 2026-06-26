"""Module for unzipping files."""

import os
from zipfile import ZipFile


def unzip_files(file_path: str, folder_path: str, remove_zip_file: bool = True):
    """Unzip file to a folder"""
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder '{folder_path}' does not exist.")

    with ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(folder_path)

    if remove_zip_file:
        os.remove(file_path)
