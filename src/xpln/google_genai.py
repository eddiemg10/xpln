from google import genai
from google.genai import types 
from rich import print  
from rich.panel import Panel 
import typer

CLIENT =  None # Google Cloud AI client global variable

SYSTEM_INSTRUCTION = """You are a command-line assistant that explains programming, scripting, and shell commands concisely.

### 🔹 Rules:  
1. **Stay within programming & command-line topics.** Ignore unrelated input.  
2. **Format responses using this structure:**  
   - **Category:** (Shell, Python, JavaScript, Docker, Git, etc.)  
   - **Purpose:** (Brief explanation of the command's function.)  
   - **Breakdown:** (Step-by-step explanation of its components.)  
   - **Example Use:** (A short, practical example.)  
   - **Caution:** (If applicable, warn about potential risks.)  
**IMPORTANT: Return the response **ONLY** as a valid JSON object following this schema:
{
    "category": required string,
    "purpose": required string,
    "breakdown": optional string,
    "example": required string,
    "caution": optional string
}
An example is:
{
    "category": "Shell",
    "purpose": "Change the current working directory.",
    "breakdown": "The cd command followed by the directory path changes the current directory to the specified path.",
    "example": "cd /home/user/Documents",
    "caution": "Be careful not to delete or overwrite important files."
}
3. **Limit responses to 100 words.**  
4. **If input is not a command, return:**  
   🚫 "Command not recognized. Did you mean something else?" 
   In this case, DO NOT return a JSON object.
5. **Do NOT execute, assume, or hallucinate responses.**  

Only return structured responses. Do not add unnecessary information.
"""

def initializeClient(api_key: str):
    """Initialize the Google Cloud AI client."""
    global CLIENT
    if CLIENT is not None:
        return CLIENT
    try:
        CLIENT = genai.Client(api_key=api_key)
        return CLIENT
    except Exception:
        print(Panel("❌ [red1]Could not initialize Google Cloud AI agent with the provided API Key.[/]\nRun xpln init --update to update the API Key.", expand=False))
        raise typer.Exit()
    

def getXplnation(command: str):
    """Get explanation for the given command."""
    global CLIENT
    global SYSTEM_INSTRUCTION

    response = CLIENT.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.2,  # Lower = more deterministic, precise answers.
            max_output_tokens=250,  # Keeps the response short and structured.
            top_p=0.9,  # Encourages diverse but reasonable word choices.
            frequency_penalty=0.3,  # Prevents repetitive explanations.
        ),
        contents=f"\n\nThe Command to explain: {command}",
    )
    return response.text