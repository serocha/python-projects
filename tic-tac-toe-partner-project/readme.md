# Tic-Tac-Toe
<!-- I did this in markdown. Feel free to edit or yell at me for making it too complicated. -->

<p>This project aims to recreate the game of tic-tac-toe within Python.</p>
<br>

## Instructions
---
<br>
<p>On starting the application, enter any keypress to start the game.</p>
<p>The game board will be drawn. If the computer was chosen to go first, you'll see that an <strong>O</strong> has already been placed. Rows are marked by numbers and columns are marked by letters.</p> 
<p>To make a move, you'll first be asked to enter a column ID, followed by a row ID. Afterward your move will be registered to the board.</p>
<p>You and the computer take turns until someone wins or there are no moves left to make. The game will then exit to the menu where you can see your session stats.</p>
<br>

## Final Results
---
<br>
<p>Something something something....</p>
<br>

## How Tasks Were Divided
---
<br>
<p>My partner designed the core game loop and mechanics, while I created the board display and the opponent algorithm.</p>
<br>

## Time Spent and Tools Used
---
Discord was used to coordinate and pass files back and forth.
<br><br>

## Technical Challenges
---
### Something
<p>Something something something....</p> <!-- placeholder sections -->
<br>

### Something
<p>Something something something....</p>
<br>

### opponent_move( )
<p>Some time was spent reading about minmax algorithms. The final function is a simplified version that prioritizes finding a winning move or preventing a losing move. If neither exists, the function recursively passes each move as a new game board, essentially simulating up to 2 turns ahead.</p>
<p>There's a bug where eval_move( ) returns NoneType. The source hasn't been found, but it has been accounted for.</p>
<br>

### draw_board( )
<p>Both the symbols and the game board span multiple output lines. A decent amount of time was spent investigating how to smash multiline strings together line-by-line. In the end, a very useful StackExchange was found that offered a solution to zipper elements onto an existing string.</p>
<br>

### parse_win( )
<p>The original concept was to have the winning combination flash for the user. Solving this without adding module dependencies proved elusive. In the end, ANSI color codes were used and the blinking was scrapped.</p>
<p>A bug was introduced here: the function copied the board to swap out winning symbols, but it was only a shallow copy. The data stored in the actual board was being mutated, which caused issues in the main application.</p>


