# tictctoe
All logic to creating the tictactoe game
Write Tictactoe using tkinter and itertools
the itertools helps using combination(a bit of math) to iterate our result to check if the returned geometry is a winning position
There are only 8 possible winning combinations.
The basic idea here is that the games playarea can be modelled as a tkinter grid and thus has geometries we can take advantage of
We create a class that when initiated creates button that populates the individual 3 by 3 grid and this button responds when clicked to either be configured to X or O.
3 different frames were created because we are dealing with pack and grid which have different masters.
The pack is used for the restart button and the label while the grid is used for the play area
The game ends when there is a winner or a draw and the game restarts
Follow the code as my comment has been added to important parts of the code in the main.py
enjoy!
