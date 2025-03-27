import typer
from functools import wraps
from xpln import FILE_ERROR
from xpln.utils import loadApiKey
from rich import print  


def require_api_key(func):
    """
    Decorator to check if xpln has already been initialized with an API Key.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        ApiKeyResponse = loadApiKey()
        if ApiKeyResponse == FILE_ERROR:
            print("Error reading config file")
            raise typer.Abort()
        elif ApiKeyResponse is None:
            print("[red1]:key: Missing API Key \nPlease run xpln init to set one up.")
            raise typer.Exit()
        else:
            return func(*args, **kwargs)
    return wrapper