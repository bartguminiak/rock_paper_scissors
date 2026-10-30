# Rock, Paper, Scissors

A small command-line Rock, Paper, Scissors game written in Python.

The project is an example of a simple object-oriented design, with game rules encapsulated in dedicated classes and a separate entry point responsible for the game flow.

## How it works

The game simulates a match between two randomly selected moves:

- Rock
- Paper
- Scissors

Each round awards one point to the winner, subtracts one point from the loser's score, or leaves the score unchanged in case of a draw.

The match continues until one side reaches a score of **+3 or -3**.

## Project structure

```text
rock_paper_scissors/
├── item.py    # Move definitions and comparison rules
├── game.py    # Game state, random move selection and scoring
└── play.py    # Command-line interface and game loop
```

### Design

- **Object-oriented design** – an abstract `Item` base class with concrete `Rock`, `Paper` and `Scissors` implementations.
- **Encapsulated game logic** – the `Game` class manages rounds, scores and match state.
- **Separation of concerns** – move comparison, game mechanics and command-line interaction are kept in separate modules.

## Requirements

- Python 3

## Getting started

Clone the repository:

```bash
git clone https://github.com/bartguminiak/rock_paper_scissors.git
cd rock_paper_scissors
```

Run the game:

```bash
python3 play.py
```

## About

A small Python project exploring object-oriented programming and basic game logic.
