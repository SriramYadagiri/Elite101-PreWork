class Board:
    def __init__(self, cols, rows):
        self.board = []
        self.player = "X"
        self.cols = cols
        self.rows = rows
        for i in range(cols*rows):
            self.board.append(" ")

    def get_move(self, bot):
        valid = False
        spot = False
        while not valid:
            try:
                spot = int(input('Pick a spot: '))-1
                if not(spot>-1 and spot<9 and self.board[spot] == " "): raise ValueError
                valid = True
            except ValueError:
                print('Please input a valid spot')
        self.board[spot] = self.player
        if not bot:
            self.player = "O" if self.player == "X" else "X"

    def equals3(self, a, b, c):
        return a != " " and a == b and b == c

    def get_winner(self):
        # vertical and horizontal
        for i in range(3):
            if self.equals3(self.board[i+(0*self.cols)], self.board[i+(1*self.cols)], self.board[i+(2*self.cols)]): return self.board[i]
            if self.equals3(self.board[0+(i*self.cols)], self.board[1+(i*self.cols)], self.board[2+(i*self.cols)]): return self.board[i]

        # diagonals
        if self.equals3(self.board[0], self.board[4], self.board[8]): return self.board[0]
        if self.equals3(self.board[2], self.board[4], self.board[6]): return self.board[2]

        for spot in self.board:
            if spot == " ": return " "

        return "tie"

    def draw(self):
        for i in range(self.cols):
            string = ""
            for j in range(self.rows):
                if self.board[j+(i*self.cols)] != " ": string += self.board[j+(i*self.cols)]
                else: string += str(j+(i*self.cols)+1)
                if j != self.cols-1: string += " | "

            print(string)
            if i != self.rows-1: print("---------")
            else: print("")