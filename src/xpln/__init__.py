"""
Top-level package for xpln.
"""
import os
from pathlib import Path

__app_name__ = "xpln"
__version__ = "0.1.0"

# Config file
# Get XDG_CONFIG_HOME or fall back to ~/.config/
CONFIG_DIR = Path(os.getenv("XDG_CONFIG_HOME", Path.home() / ".config")) / "xpln"
CONFIG_PATH = CONFIG_DIR / "config"
API_KEY = None
# Error codes for the cli
(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    NO_COMMAND_ERROR
) = range(4)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    NO_COMMAND_ERROR: "no command provided",

}

from .cli import * 