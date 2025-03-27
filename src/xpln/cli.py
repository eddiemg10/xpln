from typing import Optional, List

import time
import sys
import typer
import click
from typing_extensions import Annotated
from rich import print  
from rich.panel import Panel  
from rich.progress import Progress, SpinnerColumn, TextColumn
from pathlib import Path

from xpln.decorators import require_api_key
from xpln.utils import loadApiKey, printExplanationPanel, saveApiKey, showLandingPage
from xpln.google_genai import getXplnation, initializeClient
from . import __app_name__, __version__, FILE_ERROR, NO_COMMAND_ERROR, ERRORS

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback(invoke_without_command=True)
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    ctx = click.get_current_context()
    hasPipedInput = not sys.stdin.isatty()

    if ctx.invoked_subcommand is None:  # ✅ Only run if no subcommand was provided
       showLandingPage()

@app.command()
def init(
    api_key: Annotated[str, typer.Option(
        "--key",
        "-k",
        help="API Key"
    )]=None,
    update: Annotated[bool, typer.Option(
        "--update",
        "-u",
        help="Update API Key if one exists"
    )]=False,
) -> None:
    """
    Initialize xpln.
    """
    # Check whether API Key has already been initialized in env var, else prompt user for input
    ApiKeyResponse = loadApiKey()
    if ApiKeyResponse == FILE_ERROR:
        print("Error reading config file")
        raise typer.Abort()
    elif ApiKeyResponse is not None and not update:
        print("[green1]xpln has already been initialized with an API Key :white_heavy_check_mark:[/]")
        print(Panel("Run xpln init --update to update the API Key.", expand=False))
        raise typer.Exit()
    else:
        if not api_key:
            print(":information_source:  xpln uses Google AI Studio. Get an API Key from [link=https://aistudio.google.com/apikey][bright_cyan underline]here[/][/link]")
            api_key = typer.prompt("Enter your API Key")
        saveApiKey(api_key) 
        print(f"[green1]API Key {api_key} has been {'saved' if not update else 'updated'} successfully :white_heavy_check_mark:")


@app.command(context_settings={"ignore_unknown_options": True})
@require_api_key
def this(
    command: List[str] = typer.Argument(
        None,
        help="The Command to be explained."
    )
)->None:
    """
    Explain this command.
    """
    hasPipedInput = not sys.stdin.isatty()

    # Check if input was piped
    if hasPipedInput:
        full_command = sys.stdin.read().strip()
    elif command is not None:
        full_command = " ".join(command)
    else:
        print(f"[red]❌ {ERRORS[NO_COMMAND_ERROR]}")
        raise typer.Abort()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(description=(f"🔍 Processing..."), total=None)
        initializeClient(loadApiKey())
        explanation = getXplnation(full_command)
        progress.stop()
        printExplanationPanel(explanation)


