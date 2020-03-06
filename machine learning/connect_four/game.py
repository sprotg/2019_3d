class Connect_four_game:

    def __init__(self):
        self.reset()
        #States:
        # 0: start
        # 1: player 1
        # 2: check for win?
        # 3: player 2
        # 4: check for win?
        # 5: game over
        # 6: reset game

    def reset(self):
        self.grid = [[0 for i in range(6)] for i in range(6)]
        self.state = 0


    def place(self, col):
        if self.state == 1 or self.state == 3:
            if self.grid[col][0] == 0:
                #Valid move
                i = 5
                while self.grid[col][i] != 0:
                    i -= 1
                self.grid[col][i] = self.turn()
                self.state += 1

    def win(self):
        #Check for win
        #Vandret
        for y in range(6):
            for x in [0,1,2]:
                if (self.grid[y][x] == self.grid[y][x+1] ==
                self.grid[y][x+2] ==
                self.grid[y][x+3]) and self.grid[y][x] != 0:
                    return self.grid[y][x]
        return False

    def turn(self):
        if self.state < 3:
            return 1
        else:
            return 2
