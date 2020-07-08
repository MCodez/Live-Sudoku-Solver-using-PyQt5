# Sudoku-Solver
This code solves the n x n Sudoku grid using Backtracking algorithm.


## Algorithm
Code solves the Sudoku board rowise. It start solving from index (0, 0) till (n-1, n-1). Code searches for the empty cells (denoted by 0) and finds the best possible fit/number (from 1 to 9) for that cell without violating any contraints.

### Constraints :-
1. Each Row should have 1 - 9 numbers instantiated once.
2. Each Column should have 1 - 9 numbers instantiated once.
3. Each Box (in present scenario, 3 x 3 box) should have 1 - 9 numbers instantiated once.

In case, it did not find any probable fit for the cell, it backtraces to last solved cell and re-solve it for some other probable fit number. Backtracking is continued with the help of Recursive Function. 

Code tries to fill Sudoku board completely with exit parameters ( row = -1 and column = -1 ).

## Testbench

Code is tested on finest created Sudoku board. Images are attached below. It took around <b> 1.54 seconds </b> in solving the Board correctly. 

<img src="https://github.com/MCodez/Sudoku-Solver/blob/master/sudoku_test.png" width="250" height="250" />     <img src="https://github.com/MCodez/Sudoku-Solver/blob/master/sudoku_solution.png" width="250" height="250" />

## LIVE Sudoku Solver 

This is an advancement to the previous code. Code has been updated to provide real time Sudoku board solution by computer. Computer will show the alogirthm in lively session. One can watch how Backtracking is working in solving the Sudoku. PyQt5 QGridLayout used for generation of Sudoku Board ( 9 x 9 Grid) and QThread for computing the algorithm on separate thread and running GUI on separate thread. Check out the Board image before and after solving the Sudoku.

<img src="https://github.com/MCodez/Sudoku-Solver/blob/master/sudoku_gui_test.jpeg" width="300" height="300" />     <img src="https://github.com/MCodez/Sudoku-Solver/blob/master/sudoku_gui_solution.jpeg" width="300" height="300" />
