import random
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
import time

console = Console()

# --- Data Dictionaries (Mapping your Obsidian 05_Lists) ---
QUEST_ACTIONS = ["debug", "reboot", "steal", "DDoS", "social engineer"]
QUEST_TARGETS = ["the legacy mainframe", "the CEO's router", "a rogue Roomba", "the office coffee machine"]
NPCS = ["Clippy's Ghost", "The IT Guy", "A script kiddie", "Suspicious Printer"]
REWARDS = ["Admin Privileges", "A stale donut", "Crypto dust", "Uncommented source code"]

# Mapping your World_Events.md
EVENTS = [
    {"name": "System Update", "desc": "Everything is running 50% slower while Windows updates."},
    {"name": "Coffee Spill", "desc": "Server Room B is flooded. Hardware damage imminent!"},
    {"name": "Bountiful Ping", "desc": "Network latency is magically 0ms today."},
    {"name": "Quiet Fan", "desc": "The terminal hums quietly. Nothing unusual."}
]

class WorldState:
    def __init__(self):
        self.day = 1
        self.time_of_day = "Morning"
        self.times = ["Morning", "Afternoon", "Evening", "Night"]
        self.current_event = EVENTS[-1]
        self.active_quests = []

    # Mapping your World_Heartbeat.md
    def pass_time(self):
        idx = self.times.index(self.time_of_day)
        if idx == len(self.times) - 1:
            self.time_of_day = "Morning"
            self.day += 1
            self.current_event = random.choice(EVENTS) # Trigger random world event
            console.print(f"\n[bold cyan]--- A new cycle dawns. It is Day {self.day} ---[/bold cyan]")
            console.print(f"[bold yellow]World Event:[/bold yellow] {self.current_event['name']} - {self.current_event['desc']}")
        else:
            self.time_of_day = self.times[idx + 1]
            console.print(f"\n[dim]Cron jobs execute... Time passes. It is now {self.time_of_day}.[/dim]")

    # Mapping your Procedural_Quest_Template.md
    def generate_quest(self):
        action = random.choice(QUEST_ACTIONS)
        target = random.choice(QUEST_TARGETS)
        giver = random.choice(NPCS)
        reward = random.choice(REWARDS)

        quest_name = f"The {target.title()} Job"
        desc = f"{giver} wants you to {action} {target}. Reward: {reward}."

        self.active_quests.append({"name": quest_name, "giver": giver, "desc": desc})
        console.print(f"\n[bold green]+ New Ticket Submitted![/bold green] {quest_name}")

# Mapping your Player_Dashboard.md
def show_dashboard(world, player_name):
    console.print("\n")
    # Simulation of your Global State YAML
    table = Table(title=f"Terminal Dashboard - sysadmin: {player_name}")
    table.add_column("System Variable", style="cyan")
    table.add_column("Current State", style="magenta")

    table.add_row("Uptime", f"Day {world.day} | {world.time_of_day}")
    table.add_row("Active World Event", f"{world.current_event['name']}")

    console.print(table)

    # Simulation of your Dataview Quest Query
    if world.active_quests:
        q_table = Table(title="Open Tickets (Dataview Simulation)")
        q_table.add_column("Quest Name", style="bold white")
        q_table.add_column("Client (Giver)", style="blue")
        q_table.add_column("Details", style="dim")
        for q in world.active_quests:
            q_table.add_row(q['name'], q['giver'], q['desc'])
        console.print(q_table)
    else:
        console.print("[dim]No active tickets. Run 'scan' to find work.[/dim]")

def main_loop(name=None):
    console.clear()
    console.print(Panel("[bold blue]ZORK: THE UBUNTU CHRONICLES[/bold blue]\n[italic]A Headless Terminal Engine[/italic]", expand=False))

    if not name:
        name = Prompt.ask("\nEnter your sysadmin name", default="Root")
    world = WorldState()

    playing = True
    while playing:
        # The core interaction loop
        action = Prompt.ask(
            "\n[bold]Command Line[/bold] (dash, time, scan, quit)",
            choices=["dash", "time", "scan", "quit"],
            default="dash"
        )

        if action == "dash":
            show_dashboard(world, name)
        elif action == "time":
            world.pass_time()
        elif action == "scan":
            console.print("[dim]Scanning local network for vulnerabilities...[/dim]")
            time.sleep(1)
            world.generate_quest()
        elif action == "quit":
            console.print("[bold red]Connection Terminated. Logging off.[/bold red]")
            playing = False

if __name__ == '__main__':
    main_loop()
