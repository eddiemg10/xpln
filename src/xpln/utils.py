from . import CONFIG_DIR, CONFIG_PATH, FILE_ERROR, API_KEY
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import json

def loadApiKey():
    """Load API key from the config file and cache it."""
    global API_KEY
    if API_KEY is not None:  # If already loaded, return it
        return API_KEY

    if CONFIG_PATH.exists():
        try:
            API_KEY = CONFIG_PATH.read_text().strip()
            return API_KEY
        except Exception:
            return FILE_ERROR  # Error reading config file
    return None  # Config path does not exist

def saveApiKey(key):
    """Save API key to config file."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
    CONFIG_PATH.write_text(key.strip())  # Save the key
    global API_KEY 
    API_KEY = key  # Cache the key

def updateApiKey(key):
    """Update API key in config file."""
    saveApiKey(key)
    API_KEY = key  # Cache the key

def showLandingPage():
    console = Console()

    title = Text("🚀 [blink magenta2]Welcome to xpln![/]")
    subtitle = Text("💡 [green]xpln = Explain Before I Run[/]")

    description = Text(
        "\n🔍 Instantly get explanations for any command you run on the terminal.\n"
        "📖 Just paste a command, and let xpln break it down for you!\n",
        style="white",
        justify="center"
    )

    cta = Text(
        "\n⚙️ Run: [cyan]xpln init[/cyan] to set up your API key\n"
        "📜 Need help? Run [cyan]xpln --help[/cyan] to see available commands",
        style="yellow",
        justify="center"
    )

    panel = Panel.fit(
        f"\n{title}\n{subtitle}\n{description}\n{cta}\n",
        border_style="bright_blue",
        padding=(1, 2)
    )

    console.print(panel)

def cleanJson(response_text: str) -> str:
    """Removes code block formatting (e.g., ```json ... ```) from the response."""
    return response_text.strip("```json").strip("```").strip()

def printExplanationPanel(explanation: str):
    console = Console()
    try:
        # ✅ Attempt to parse JSON
        data = json.loads(cleanJson(explanation))

        # 🔹 Iterate and print each key-value pair
        output = ""
        for key, value in data.items():
            # Special case for caution: Add ⚠️ emoji if present
            if key == "caution":
                output += f"\n[orange_red1]⚠️ {key.capitalize()}: {value} [/]\n"
                continue
            
            output += f"[cyan]🔹 {key.capitalize()}:[/] {value}\n"

        # 📌 Wrap everything in a rich panel
        console.print(Panel(output.strip(), border_style="magenta2"))

    except json.JSONDecodeError:
        # 🚨 If JSON parsing fails, print as-is (for non-commands)
        console.print(Panel(explanation, border_style="yellow"))