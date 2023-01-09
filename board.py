class Board:
    def __init__(self):
        self.fills = [0] * 7
        self.board = []
        self.player = "X"
        for i in range(7):
            self.board.append(["."] * 6)

    def printBoard(self):
        for i in range(5, -1, -1):
            print("|", end="  ")
            for j in range(7):
                print(self.board[j][i], end="  ")
            print("|")
        print("-------------------------")
        print("   0  1  2  3  4  5  6")

    def placePiece(self, column):
        if not 0 <= column <= 6:
            return False
        if self.fills[column] == 5:
            return False
        self.board[column][self.fills[column]] = self.player
        self.fills[column] += 1
        return True

    def switchPlayer(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    def bitify(self, player):
        amount = 0
        for i in range(5, -1, -1):
            for j in range(6, -1, -1):
                if self.board[j][i] == player:
                    amount += 1
                amount = amount << 1
        return amount >> 1

    def printBitified(self, player):
        bitified = self.bitify(player)
        for i in range(5, -1, -1):
            print("|", end="  ")
            for j in range(6, -1, -1):
                print("X" if (bitified & (2 ** ((7 * i) + (6 - j))) > 0) else ".", end="  ")
            print("|")

    def checkWin(self, column, solutions):
        row = self.fills[column] - 1
        player = self.board[column][row]
        bitified = self.bitify(player)
        for s in solutions[str((7 * row) + column)]:
            if s & bitified == s:
                return True
        return False




