# World Engine Documentation

The `world_engine.py` is the core of the text-based adventure, driving the simulation of a sysadmin's environment. It leverages `rich` for an immersive terminal-based UI and relies on a global state to handle quests, time passage, and randomized events.

## Overview
The engine serves as a **Headless Terminal Engine**. Instead of moving between traditional text adventure rooms (e.g., "Go North", "Go West"), the player interacts with a command-line simulation to view active tickets, manage time, and scan for tasks.

---

## Core Systems

### `WorldState`
The `WorldState` class maintains the global variables for the simulation.
- **`day`** *(int)*: Tracks the current uptime/day count. Starts at `1`.
- **`time_of_day`** *(str)*: A string representing the current time period.
- **`times`** *(list)*: A static list containing `["Morning", "Afternoon", "Evening", "Night"]`. Used to cycle through the day.
- **`current_event`** *(dict)*: Holds the active event affecting the game world. Contains `"name"` and `"desc"`.
- **`active_quests`** *(list)*: An array storing generated tickets/quests that the player must complete.

#### Methods
- **`pass_time(self)`**: Progresses the `time_of_day`. If the cycle reaches "Night", it wraps back around to "Morning", increments the `day` variable, and triggers a new randomized `World Event`.
- **`generate_quest(self)`**: Simulates procedural quest generation. Pulls random strings from global data dictionaries (`QUEST_ACTIONS`, `QUEST_TARGETS`, `NPCS`, `REWARDS`) to construct a "ticket" and appends it to `active_quests`.

---

### Player Dashboard (`show_dashboard`)
This function simulates a "Dataview" or global state UI.
- Retrieves the current `world` instance and the `player_name`.
- Utilizes `rich.table.Table` to output two separate tables:
  1. **Terminal Dashboard**: Displays variables such as `Uptime` (Day + Time) and `Active World Event`.
  2. **Open Tickets**: Iterates through `world.active_quests` and prints the `Quest Name`, `Client (Giver)`, and `Details`.

---

### Main Interaction Loop (`main_loop`)
The `main_loop` is the entry point for the text adventure.
- **Initialization**: Takes an optional `name` argument. If not provided, it prompts the user. Instantiates a new `WorldState`.
- **Game Loop**: A continuous `while playing` loop running a `Prompt.ask` waiting for input.
- **Commands**:
  - `dash`: Calls `show_dashboard()`.
  - `time`: Calls `world.pass_time()`.
  - `scan`: Simulates vulnerability scanning by sleeping for 1 second, then calling `world.generate_quest()`.
  - `quit`: Terminates the connection and breaks the loop.

## Data Dictionaries
The engine utilizes several list constants to randomize content:
- **`QUEST_ACTIONS`**: Verbs or actions to perform (e.g., debug, reboot).
- **`QUEST_TARGETS`**: Objects or hardware being targeted (e.g., rogue Roomba).
- **`NPCS`**: Quest givers / Characters.
- **`REWARDS`**: The payout for completing a quest.
- **`EVENTS`**: A list of dictionary objects representing environmental modifiers (e.g., "System Update").
