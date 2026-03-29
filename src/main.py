#!/usr/bin/env python3

# Jules Code Team Template
# Copyright (C) 2026  MnemOnicE
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import logging
import sys
import uuid

# Imports
try:
    from src.core.bus import NexusBus
    from src.core.context import load_context
    from src.core.tools.graph_executor import GraphExecutor
except ImportError as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

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
    """
    Generates a static execution graph for demonstration.
    Adheres to src/core/schema/execution_graph.json
    """
    graph_id = str(uuid.uuid4())

    return {
        "graph_id": graph_id,
        "intent_glyph": "🤖",
        "aether_mark": "mock_signature_verified",
        "entry_point": "node_1",
        "context_delta": {},
        "nodes": {
            "node_1": {
                "action": "logic_gate",
                "params": {
                    "condition": "Is task valid?"
                },
                "on_success": "node_2",
                "on_failure": "node_fail"
            },
            "node_2": {
                "action": "run_tool",
                "params": {
                    "tool": "plan_decomposition",
                    "args": {"task": task_description}
                },
                "on_success": "node_4"
            },
            "node_4": {
                "action": "terminate",
                "params": {}
            },
            "node_fail": {
                 "action": "terminate",
                 "params": {}
            }
        }
    }

def main():
    parser = argparse.ArgumentParser(description="Agent System V3 Command Interface")
    parser.add_argument("--task", type=str, help="The natural language task to perform")
    parser.add_argument("--file", type=str, help="A file to process")

    args = parser.parse_args()

    if not args.task and not args.file:
        # Default behavior: run the game
        start_game()
        sys.exit(0)

    task = args.task or f"Process file: {args.file}"

    # Configure centralized logging
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(name)s: %(message)s'
    )

    print("\n🔮 \033[1mInitializing Agent System V3...\033[0m")

    # 1. Initialize Bus (Nervous System)
    try:
        bus = NexusBus()
        print("✅ NexusBus Online")
    except Exception as e:
        print(f"❌ Failed to initialize NexusBus: {e}")
        # Continue mostly, or exit?
        # If bus fails (e.g. schema missing), we should probably fail.
        sys.exit(1)

    # 2. Load Context (Cortex Loader)
    try:
        brain_context = load_context("brain")
        print(f"✅ Loaded Persona: {brain_context['role']}")
    except Exception as e:
        print(f"❌ Failed to load context: {e}")
        sys.exit(1)

    # 3. Generate Execution Graph (Brain)
    print(f"🧠 Brain: Analyzing task: '{task}'")
    graph = generate_mock_graph(task)
    print(f"✅ Generated Execution Graph ({graph['graph_id']})")

    # 4. Execute (Muscles)
    print("\n🚀 \033[1mExecuting Graph...\033[0m")
    executor = GraphExecutor(bus)
    executor.execute(graph)

    print("\n✨ Mission Complete.")

if __name__ == "__main__":
    main()
