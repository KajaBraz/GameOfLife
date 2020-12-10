# GameOfLife
My implementation of The Game of Life - the program that simulates the evolution.

Rules of the game:
- There is a board of size N by N, in which each cell can be active (alive) or inactive (dead)
- Each cell can have 8 neighbours (top -> 1, bottom -> 1, left -> 1, right -> 1 and diagonally -> 4)
- The program executes in turns; each turn observes the following two rules:
  1. If the cell is active and has 2 or 3 active neighbours, it remains active in the next turn, otherwise its state changes
  2. If the cell is inactive and it has exactly 3 active neighbours, it becomes active in the next turn, otherwise it remains inactive

The sample files show the states of the given tables with cells in many stages (table 1 is random, table 2 is created manually so that it ends at a certain point). You can notice there the evolution process of the given population (cells).

To know more:
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
