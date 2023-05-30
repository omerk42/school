import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fiscoreXpot(self, row, col, player):
        self.board[row][col] = player

    def score(self, turn):
        path = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]]
        ]
        xSc = 0
        ySc = 0
        for i in path:
            conf = False
            for j in i:
                if (turn[j[0]][j[1]] == 'O'):
                    conf = True
            if (not conf):
                xSc = xSc + 1

        for i in path:
            conf = False
            for j in i:
                if(turn[j[0]][j[1]] == 'X'):
                    conf = True
            if(not conf):
                ySc = ySc + 1
        return xSc, ySc
    
    def is_player_win(self, player):
        win = None

        n = len(self.board)
        
        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
    

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win
        
        win = True
        for i in range(n):
            if self.board[i][2-i] != player:
                win = False
                break
        if win:
            return win

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True
    
    def evaluateMaxMin(self):
        boardLim = 3
        maxS = []
        scoreMid = 0
        for i in range(boardLim):
            for j in range(boardLim):
                if (self.board[j][i] != '-'):
                    continue
                else:
                    newBoar = self.board[:]
                    newBoar[j][i] = 'X'
                    scoreX, scorey = self.score(newBoar)
                    newBoar[j][i] = '-'
                    if (scoreX - scorey > scoreMid):
                        scoreMid = scoreX - scorey
                        maxS = [j, i]
        if len(maxS) == 0:
            for i in range(boardLim):
                for j in range(boardLim):
                    if(self.board[i][j] == '-'):
                        return [i, j]
        return maxS

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()
        print("you are O , Start playing")

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            if (player == 'O'):
                # taking user input
                while True:
                    try:
                        row, col = list(
                            map(int, input("Enter row and column numbers to fix spot: ").split()))
                        break
                    except Exception as e:
                        print(e)
                print()

            if (player == 'X'):
                p = self.evaluateMaxMin()
                row = p[0] + 1
                col = p[1] + 1

            # fixing the spot
            self.fiscoreXpot(row - 1, col - 1, player)
           
            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()




# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()