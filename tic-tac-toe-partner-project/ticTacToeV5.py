'''
This is a tic-tac-toe program
I received help from Shane Rocha in designing and debugging my program as this was a group project.
I spent 4 hours on this program.
'''
import render
import art
import random
import os
import opponent

global theBoard #set the game board to a global variable
global playerScore
global computerScore
global ties
playerScore = 0
computerScore = 0
ties = 0
theBoard = [[art.EMPTY, art.EMPTY, art.EMPTY], [art.EMPTY, art.EMPTY, art.EMPTY], [art.EMPTY, art.EMPTY, art.EMPTY]]  #starting condition of the game board

def startGame(): #this starts off the game with a quick explaination
	os.system('cls')
	print('Welcome to the Tic-Tac-Toe Game. ')
	print('You are Xs and the computer are Os')
	print("The player going first is randomized.")
	print("Player Score: ", playerScore)
	print("Computer Score: ", computerScore)
	print("Ties: ", ties)
	startGaming = input("Press any letter to start! ")
	if startGaming != "":
		modifyBoard() 
	else:
		startGame()

def modifyBoard():  #function that modifies the gameboard
	winnerWinner = False
	userLoser = False  
	userTie = False 
	loop = True #variable to loop condition
	gameTurn = random.randint(0,1)  #variable that determines whose turn it is
	while loop == True:
		os.system('cls') #clear the terminal window
		print(art.logo)
		render.draw_board(theBoard)
		try:
			if gameTurn % 2 == 0: #if even, then players turn
				#player inputs column
				playerInputColumn = input("Please enter the column of your next move (i.e. A, B, C): ") 
				if playerInputColumn == 'A' or playerInputColumn == 'a': #change variables to a number to help with dealing with lists
					playerInputColumn = 0
				elif playerInputColumn == 'B' or playerInputColumn == 'b':
					playerInputColumn = 1
				elif playerInputColumn == 'C' or playerInputColumn == 'c':
					playerInputColumn = 2
				else:
					pass
				#player inputs Row
				playerInputRow = int(input("Please enter the row of your next move (i.e. 1, 2, 3): "))
				if playerInputRow == 1: #change variables to a number to help with dealing with lists
					playerInputRow = 0
				elif playerInputRow == 2:
					playerInputRow = 1
				elif playerInputRow == 3:
					playerInputRow = 2
				elif playerInputRow < 0 or playerInputRow > 3:
					pass
				else:
					pass
			
				if theBoard[playerInputRow][playerInputColumn] != art.X and theBoard[playerInputRow][playerInputColumn] != art.O: #checks the space the player input for an x or o
					theBoard[playerInputRow][playerInputColumn] = art.X #add x to space the player chose
					gameTurn += 1
					if testWinCondition() == True: #if testWinCondition returns true, the player has won
						gameTurn = 0
						winnerWinner = True
						loop = False
						break
					elif testTieCondition() == True:
						userTie = True
						loop = False
						break
				else:
					pass
		except TypeError:	
			print('')	
		except IndexError:	
			print('')	
		except ValueError:	
			print('')	
			
		if gameTurn % 2 != 0:  #computer's turn on odd
			opponent.opponent_move(theBoard) #call opponent_move module for computer moves
			gameTurn += 1 #add to variable to change turn
			if testLoseCondition() == True: #if testLoseCondition returns true, the player has lost
				userLoser = True
				loop = False
				break
			elif testTieCondition() == True:
				userTie = True
				loop = False
				break
	if winnerWinner == True:
		playerVictory()
	elif userLoser == True:
		playerLoss()
	elif userTie == True:
		playerTie()
	

def testWinCondition():  #win conditions for player win
	if theBoard[0][0] == art.X and theBoard[1][0] == art.X and theBoard[2][0] == art.X:
		return True
	elif theBoard[0][1] == art.X and theBoard[1][1] == art.X and theBoard[2][1] == art.X:
		return True
	elif theBoard[0][2] == art.X and theBoard[1][2] == art.X and theBoard[2][2] == art.X:
		return True
	
	elif theBoard[0][0] == art.X and theBoard[0][1] == art.X and theBoard[0][2] == art.X:
		return True
	elif theBoard[1][0] == art.X and theBoard[1][1] == art.X and theBoard[1][2] == art.X:
		return True
	elif theBoard[2][0] == art.X and theBoard[2][1] == art.X and theBoard[2][2] == art.X:
		return True
	
	elif theBoard[0][0] == art.X and theBoard[1][1] == art.X and theBoard[2][2] == art.X:
		return True
	elif theBoard[0][2] == art.X and theBoard[1][1] == art.X and theBoard[2][0] == art.X:
		return True
	else:
		return False
	
def testLoseCondition(): #win conditions for player loss
	if theBoard[0][0] == art.O and theBoard[1][0] == art.O and theBoard[2][0] == art.O:
		return True
	elif theBoard[0][1] == art.O and theBoard[1][1] == art.O and theBoard[2][1] == art.O:
		return True
	elif theBoard[0][2] == art.O and theBoard[1][2] == art.O and theBoard[2][2] == art.O:
		return True
	
	elif theBoard[0][0] == art.O and theBoard[0][1] == art.O and theBoard[0][2] == art.O:
		return True
	elif theBoard[1][0] == art.O and theBoard[1][1] == art.O and theBoard[1][2] == art.O:
		return True
	elif theBoard[2][0] == art.O and theBoard[2][1] == art.O and theBoard[2][2] == art.O:
		return True
	
	elif theBoard[0][0] == art.O and theBoard[1][1] == art.O and theBoard[2][2] == art.O:
		return True
	elif theBoard[0][2] == art.O and theBoard[1][1] == art.O and theBoard[2][0] == art.O:
		return True
	else:
		return False
	
def testTieCondition():  #tests to see if the game is tied
	emptySpaces = 0
	for i in theBoard:
		for j in i:
			if j == art.EMPTY:
				emptySpaces =+ 1
	if emptySpaces > 0: #return true if an empty spot if found
		return False
	else:
		return True

def playerVictory():  #player victory and ask user to play again
	global playerScore
	os.system('cls') #clear the terminal window
	print(art.logo)
	render.draw_board(theBoard)
	print("You have won!")
	playerScore += 1
	playAgain = input("Do you want to play again? ('Y'es or 'N'o) ")
	if playAgain == 'Y' or playAgain == 'y' or playAgain == 'Yes' or playAgain == 'yes':
		render.clear_board(theBoard)
		startGame()
	elif playAgain == 'N' or playAgain == 'n' or playAgain == 'No' or playAgain == 'no':
		exit()
	else:
		render.clear_board(theBoard)
		startGame()

def playerLoss(): #player loss and ask user to play again
	global computerScore
	os.system('cls')
	print(art.logo)
	render.draw_board(theBoard)
	print("You have lost!")
	computerScore += 1
	playAgain = input("Do you want to play again? ('Y'es or 'N'o) ")
	if playAgain == 'Y' or playAgain == 'y' or playAgain == 'Yes' or playAgain == 'yes':
		render.clear_board(theBoard)
		startGame()	
	elif playAgain == 'N' or playAgain == 'n' or playAgain == 'No' or playAgain == 'no':
		exit()
	else:
		render.clear_board(theBoard)
		startGame()
def playerTie():  #player tie and ask user to play again
	global ties
	os.system('cls')
	print(art.logo)
	render.draw_board(theBoard)
	print("You have tied!")
	ties += 1
	playAgain = input("Do you want to play again? ('Y'es or 'N'o) ")
	if playAgain == 'Y' or playAgain == 'y' or playAgain == 'Yes' or playAgain == 'yes':
		render.clear_board(theBoard)
		startGame()	
	elif playAgain == 'N' or playAgain == 'n' or playAgain == 'No' or playAgain == 'no':
		exit()
	else:
		render.clear_board(theBoard)
		startGame()



if __name__ == '__main__':
	startGame()	



