# Python Copilot for World of Warcraft AH

This project provides an interactive command-line tool to analyze World of Warcraft Auction House (AH) data for mounts. It leverages the TradeSkillMaster (TSM) API to fetch up-to-date pricing for mounts on a specific realm and auction house, then uses a local LLM (Ollama) to summarize key info in a user-friendly way.

## Features

- Select a mount by name from a curated list (`mounts.json`)
- Fetch current market value, historical price, minimum buyout, and number of active auctions using TSM APIs
- Summarize results using an LLM, with prices formatted for WoW (gold, silver)
- Presents results in a clear, colorful table (using `rich`)

## Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) for package management
- A local [Ollama](https://ollama.com/) setup for LLM-powered summaries (model: `llama3.2`)
- TSM API token stored in a `.env` file

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Kuba123pl/python-copilot-for-world-of-warcraft-AH.git
    cd python-copilot-for-world-of-warcraft-AH
    ```

2. Install dependencies with uv:
    ```bash
    uv pip install -r requirements.txt
    ```
    Or, using `pyproject.toml`:
    ```bash
    uv pip install -r pyproject.toml
    ```

3. Create a `.env` file in the root directory and add your TSM API token:
    ```
    TOKEN=your_tsm_api_token
    ```

## Usage

1. (Optional) Activate your virtual environment if you use one.
2. Run the main script:
    ```bash
    python main.py
    ```
3. When prompted, enter the name of the mount you want info for (case-insensitive, as listed in `mounts.json`).
4. The script will fetch the latest data and display a formatted table with the market analysis.

## Project Structure

- `main.py` — The main script handling user interaction, API authentication, data fetching, and display.
- `mounts.json` — List of supported mount names and their IDs.
- `pyproject.toml` — Python project configuration and dependencies.
- `.env` — Store your TSM API token (not committed).
- `uv.lock` — Lockfile for reproducible installs with `uv`.

## Example

```
For what mount currently on AH are you interested in?
> sky golem

# (Console table output with price summary)
```

## Notes

- The tool uses the [rich](https://rich.readthedocs.io/) library for beautiful terminal output.
- Ollama LLM is required locally for natural language item summaries.
- Only mounts listed in `mounts.json` are supported.

## License

MIT License
