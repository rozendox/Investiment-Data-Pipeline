"""Configure Env Module"""

import os

from dotenv import load_dotenv


def configure_environ():
    """Configure the envoriment variables."""
    load_dotenv(f'{os.getcwd()}/.env', verbose=False)
