from board import Board
import json

board = Board()
with open("solutions.json", "r") as readFile:
    solutions = json.load(readFile)
while(True):
    board.printBoard()
    column = int(input(f"Your move, {board.player}!: "))
    if not board.placePiece(column):
        print(f"Invalid move! Try again, {board.player}!")
        continue
    if board.checkWin(column, solutions):
        board.printBoard()
        print(f"You win, {board.player}!!!")
        break
    board.switchPlayer()










