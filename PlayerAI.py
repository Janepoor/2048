###############################################
# #!/usr/bin/env python
# #coding:utf-8
#jm4437  Jianpu Ma

#####################################
#####################################


import sys
from BaseAI import BaseAI
from random import randint

MAX_VALUE = sys.maxint
MIN_VALUE = -MAX_VALUE
depth_limit = 4

class PlayerAI(BaseAI):

    def getMove(self, grid):
        return self.player(MIN_VALUE, MAX_VALUE, grid, depth_limit)[1]


    def player(self, alpha, beta, grid, depth):


        if depth == 0 or not grid.canMove():
            return [self.score(grid), None]

        v = MIN_VALUE
        nextstates = []
        nextmove = grid.getAvailableMoves()
        for action in nextmove:
            newGrid = grid.clone()
            newGrid.move(action)
            temp = [newGrid, action]  # stores each new state and the corresponding move
            nextstates.append(temp)

        for s in nextstates:
            nextgrid=s[0]
            vtmp = self.computer(alpha, beta, nextgrid, depth - 1)

            if vtmp > v:
                v = vtmp
                bestMove = s[1]
            if v >= beta:
                return [v, bestMove]

            alpha = max(alpha, v)

        return [v, bestMove]

    def computer(self, alpha, beta, grid, depth):

        if depth == 0 or not grid.canMove():
            return [self.score(grid), None]

        v = MAX_VALUE
        nextstates = []
        Emptycell = grid.getAvailableCells()

        for p, q in Emptycell:
            newGrid = grid.clone()

            if randint(0,99) < 90: 
                newGrid.map[p][q] = 2
            else:
                newGrid.map[p][q] = 4 

            nextstates.append(newGrid)

        for m, n in Emptycell:
            newGrid = grid.clone()
            if randint(0,99) < 90: 
                newGrid.map[m][n] = 2
            else:
                newGrid.map[m][n] = 4 
            nextstates.append(newGrid)

        for s in nextstates:
            v = min(v, self.player(alpha, beta, s, depth - 1)[0])

            if v <= alpha:
                return v
            beta = min(beta, v)

        return v



   #That is the number in the corner is assigned the biggest weight.
    def score(self,grid):

    #########################################################################################################
    # Part I     The heuristic score for the empty tile, each weight 1
    ########################################################################################################
        emptyblock_score = len(grid.getAvailableCells())

    ##########################################################################################################
    # Part II     The heurisic score for the snake, each weight according to the weight list by pow function
    #########################################################################################################

        weight = []
        for i in xrange(16):
            weight.append(pow(0.125, i))

        snakeorder=[grid.map[0][0], grid.map[0][1], grid.map[0][2], grid.map[0][3],
                  grid.map[1][3], grid.map[1][2], grid.map[1][1], grid.map[1][0],
                  grid.map[2][0], grid.map[2][1], grid.map[2][2], grid.map[2][3],
                  grid.map[3][3], grid.map[3][2], grid.map[3][1], grid.map[3][0]]
        
        score1=0
        for i in xrange(16):
            
            score1+=snakeorder[i]*weight[i]

        if snakeorder[0] == grid.getMaxTile():  # award bonus for keeping max tile in corner
            score1 *= 1.25

        score = score1 + emptyblock_score

        return score

# measures how smooth the grid is (as if the values of the pieces were interpreted as elevations). Sums of the pairwise differencex
# between neighboring tiles (in log space, so it represents the  number of merges that need to happen before they can merge).

    """def smoothness(self,grid):
        smoothness_score=0
        current_size = grid.size

        for i in xrange(0, current_size):
            for j in xrange(0, current_size):
                if grid.map[i][j] != 0:
                    value=math.log(grid.map[i][j],2)"""









