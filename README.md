
# True or False Game

[![GitHub Release](https://img.shields.io/github/v/release/PGSch/TrueOrFalse?logo=github)](https://github.com/PGSch/TrueOrFalse/releases)
[![GitHub License](https://img.shields.io/github/license/PGSch/TrueOrFalse)](https://github.com/PGSch/TrueOrFalse/blob/main/LICENSE)
[![Sponsor](https://img.shields.io/badge/sponsor-♥-f06292)](https://github.com/sponsors/PGSch)
[![Twitter Follow](https://img.shields.io/twitter/follow/pgschdev?style=social)](https://twitter.com/intent/follow?screen_name=PGSch)

## Overview

The **True or False Game** is a command-line quiz game where players are asked random true or false questions. The game supports user authentication, score tracking, and has a leaderboard system that records user scores in a JSON file. The game server provides questions and authentication using an HTTP server.

## Features

- **User Login System**: Users authenticate with a username and password.
- **Random Questions**: The game fetches random questions from a JSON file hosted on the server.
- **Score Tracking**: User scores are saved in `scores.json` and can be viewed later.
- **Persistent Leaderboard**: The game saves and displays previous scores in a neat, readable format.
- **Reset Scores**: Users can reset the leaderboard by deleting the `scores.json` file.

## How It Works

1. **Login**: Users must provide their username and password to start playing.
2. **Random Questions**: The game fetches random true or false questions from a `questions.json` file hosted on the server.
3. **Track Scores**: After each game, the player's score is recorded in `scores.json`, including the date.
4. **View or Reset Scores**: Players can view the leaderboard or reset it by selecting the appropriate options from the menu.

## Setup Instructions

### Prerequisites

- Python 3.x
- Bash (Linux/macOS)
- `jq` (to handle JSON in bash)
  - Install via `brew install jq` on macOS.

### Installation and Running the Game

1. **Clone the repository**:

   ```bash
   git clone https://github.com/PGSch/TrueOrFalse.git
   cd TrueOrFalse
   ```

2. **Start the server**:

   Run the setup script to start the HTTP server and initialize files:

   ```bash
   ./setup.sh
   ```

   This will:
   - Create the required files and folders.
   - Start the Python HTTP server.

3. **Play the game**:

   After the server is running, open another terminal and run:

   ```bash
   ./true_or_false.sh
   ```

   You will be prompted to log in and can start answering random true or false questions!

## Files

- **`setup.sh`**: Initializes the game by creating required files and starting the server.
- **`server.py`**: The Python HTTP server that handles login and game requests.
- **`questions.json`**: Contains the questions and answers used in the game.
- **`true_or_false.sh`**: The main game logic implemented in Bash.

## Example Questions

The `questions.json` file contains questions like:

```json
[
    {
        "question": "The Great Wall of China is visible from space.",
        "answer": "False"
    },
    {
        "question": "Light travels faster than sound.",
        "answer": "True"
    }
]
```

## Leaderboard

Player scores are saved in the `scores.json` file, where each entry contains:

- **User**: The player's name.
- **Score**: The total points earned.
- **Date**: The date when the game was played.

Example entry in `scores.json`:

```json
[
    {
        "User": "Alice",
        "Score": 30,
        "Date": "2024-10-01"
    }
]
```

## Contributing

We welcome contributions to enhance the True or False Game! Please open an issue or submit a pull request for any features or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
