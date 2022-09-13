from board import Board
import bot

is_bot = True
board = Board(3, 3)

def loop():
    board.get_move(is_bot)
    if is_bot:
        bot.make_move(board)
    board.draw()
    winner = board.get_winner()
    if winner != " ":
        board.draw()
        if winner == "tie": print("It's a tie!")
        else: print(winner + " wins!")
        return
    loop()

def startGame():
  global board
  board = Board(3, 3)
  board.draw()
  loop()