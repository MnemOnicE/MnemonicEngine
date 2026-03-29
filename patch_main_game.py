<<<<<<< SEARCH
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import time
from src.world_engine import main_loop

console = Console()

def start_game():
    console.clear()

    # Generate the "DORK!" ASCII art
    ascii_art = pyfiglet.figlet_format("DORK!")
    console.print(f"[bold red]{ascii_art}[/bold red]")

    # Display a stylish game header
    console.print(Panel("[bold blue]Welcome to the ADVENTURE![/bold blue]\n[italic]An Ubuntu-powered Adventure[/italic]", expand=False))

    # Prompt for user input
    name = Prompt.ask("What is this dork's name?", default="Dweeb")

    # Boom's Logic Upgrade: Cheat code dictionary and branching age prompt
    cheat_codes = {
        "godmode": "[bold magenta]Cheat Activated: Invincibility enabled.[/bold magenta]",
        "noclip": "[bold magenta]Cheat Activated: You can now walk through walls.[/bold magenta]",
        "iddqd": "[bold magenta]Cheat Activated: Your eyes glow with a demonic energy.[/bold magenta]"
    }

    age = Prompt.ask("Who?... Hmm... How old are you?", default="old enough")

    if age == "old enough":
        secret_answer = Prompt.ask("What? Ew. For what?", default="...")

        # Check if the answer exists in our dictionary
        if secret_answer in cheat_codes:
            console.print(cheat_codes[secret_answer])
            # You can add specific variable changes here, like: player_health = 9999
        else:
            console.print("...Right. Anyway.")
    else:
        console.print(f"So you're {age}? Hmm, yeah, you definitely look old.")

    console.print(f"\nWelcome, [bold green]{name}[/bold green]. You wake up in a dark server room...\n")
    time.sleep(1)

    # Simple choice logic with built-in validation
    choice = Prompt.ask(
        "You see a glowing keyboard and a heavy metal door. What do you do?",
        choices=["type", "kick"],
        default="type"
    )

    if choice == "type":
        console.print("\n[bold yellow]Success![/bold yellow] You typed `sudo apt update` and the door unlocked.")
        time.sleep(1)
        # Transition to world engine
        main_loop(name)
    else:
        console.print("\n[bold red]Ouch![/bold red] The door is made of reinforced steel. Your toe hurts.")
        console.print("Game Over.")

def generate_mock_graph(task_description):
=======
from src.game import start_game

def generate_mock_graph(task_description):
>>>>>>> REPLACE
