# Sliding-Puzzle-Solver

Goal: Solving a 3x3 Sliding Puzzle by using A* algorithm

## Scenario:
Gameboard: a 3x3 sliding puzzle contains 3x3 cells. Here we will label the cell locations as A-I from top to bottom, left to right, i.e.,

A	B	C
D	E	F
G	H	I

We label the tiles as 1-8 for normal cell and 0 for empty cell. 

### Input
The input reads from the input stream that contains a random generated board state which is represented as a sequence of 9 digits without space.
Example: 315027684

### Output
The output should contain the move sequence to solve the given puzzle in the form of characters and each character is A-I indicating the cell locations from which the tiles should be slided to the empty cell.
Example: ABEFIHEFCBA


 
