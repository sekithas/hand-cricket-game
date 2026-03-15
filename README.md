## Hand Cricket Game

__Python Libraries__
1. Tabulate
2. Time
3. Random

## Description

Hand Cricket is a command-line cricket game written in Python where a player competes against the computer. The game simulates a simplified version of cricket where both players secretly choose a number between 0 and 6 each ball. If the numbers match, the batter is declared out. Otherwise, the batting side scores runs according to the chosen number.

The game follows a short match format:
	•	2 overs per player (12 balls)
	•	3 wickets per player
	•	A coin toss decides who bats first
	•	The second player must chase the target score

The program also includes random commentary, a scoreboard using tables, and a ball history display to make the match feel more realistic.

The program was inspired to be made after the recent T20 world cup.

## Features
- Coin toss where the player chooses heads or tails, a loading animation occurs and the winner is decided. The winner is allowed to choose whether to bat or ball first.
- The first batter sets a score, that the second batter should beat by 1 to win the game.
- There are three wickets. Each time the user and computer chooses the same number it is out.
- Each scoring shot from the batter triggers a random commentary, implemented with help of the random library, related to the run's value to simulate a cricket broadcast.
- Each inning the final score, in format (score - wickets fallen) is given in a table, created with the tabulate library.
- After an inning, the bowling history is printed, to see how the batsman scored ball-by-ball.
- After the game, the final score of the user and computer are given in a table and the match result is announced.

## File Overview
- `project.py`: consists of the core mechanism of the game, handling match flow, innings logic, scoreboard display and result calculation.
- `toss.py`: implements the coin toss system to decide who bats first and who bowls first.
- `commentaries.py`: contains randomized commentary for runs and wickets in a dictionary.
- `test_project.py`: unit tests written with pytest.

## Design choices
- An innings function was extracted to be reused in the second innings.
- The toss was optional, so was moved to a new file.
- Commentaries were also optional as it didn't relate to the core mechanism, thus were moved to a different .py file.
- Time library was used to improve UX, as the coin flip feels realistic.
- Tabulate library was used also to improve UX, as results are clearly displayed.
- Computer runs are designed to have a higher chance of playing boundaries or doubles using the random module, to make the game more challenging.

## How to play
- Simply type python project.py in your command line terminal.

## Example gameplay
```
Welcome to hand cricket!
Each player gets 2 overs | 3 wickets


Heads or tails: tails

Flipping coin.....

You won the toss!
Bat or ball?: bat


========== FIRST INNINGS ==========

You are batting now!

Runs: 6
Computer runs: 1
SIX! Launched over the boundary for a maximum.
6 - 0
Runs: 2
Computer runs: 3
They come back for the second run comfortably.
8 - 0
Runs: 6
Computer runs: 3
SIX! Launched over the boundary for a maximum.
14 - 0
Runs: 1
Computer runs: 3
Quick single taken.
15 - 0
Runs: 6
Computer runs: 0
SIX! Launched over the boundary for a maximum.
21 - 0
Runs: 6
Computer runs: 6
OUT! Straight through the gate!
Runs: 5
Computer runs: 4
Misfield leads to five runs.
26 - 1
Runs: 6
Computer runs: 1
SIX! Launched over the boundary for a maximum.
```

## install dependencies
- pip install -r requirements.txt
