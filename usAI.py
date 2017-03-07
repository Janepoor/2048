###############################################
# #!/usr/bin/env python
# #coding:utf-8
# jm4437  Jianpu Ma

#####################################
#####################################
###Reference from stackoverflow
"""smoothWeight = 0.1,
// monoWeight = 0.0,
// islandWeight = 0.0,
mono2Weight = 1.0,
emptyWeight = 2.7,
maxWeight = 1.0


this.grid.smoothness() * smoothWeight
       //+ this.grid.monotonicity() * monoWeight
       //- this.grid.islands() * islandWeight
       + this.grid.monotonicity2() * mono2Weight
       + Math.log(emptyCells) * emptyWeight
       + this.grid.maxValue() * maxWeight;


"""

import sys
import math
from BaseAI import BaseAI

MAX_VALUE = sys.maxint
MIN_VALUE = -MAX_VALUE
depth_limit = 4


class PlayerAI(BaseAI):

    def getMove(self, grid):
        return self.player(MIN_VALUE, MAX_VALUE, grid, depth_limit)[1]

    def player(self, alpha, beta, grid, depth):

        # 1 denote the player, 0 denotes the computer AI

        if depth == 0 or not grid.canMove():
            return [self.score(grid), None]

        ###### for user
        v = MIN_VALUE
        nextstates = []
        nextmove = grid.getAvailableMoves()
        for action in nextmove:
            newGrid = grid.clone()
            newGrid.move(action)
            temp = [newGrid, action]  # stores each new state and the corresponding move
            nextstates.append(temp)

        for s in nextstates:
            vtmp = self.computer(alpha, beta, s[0], depth - 1)

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

        for c in Emptycell:
            p, q = c
            newGrid = grid.clone()
            newGrid.map[p][q] = 2
            nextstates.append(newGrid)
        for d in Emptycell:
            m, n = d
            newGrid = grid.clone()
            newGrid.map[m][n] = 4
            nextstates.append(newGrid)

        for s in nextstates:
            v = min(v, self.player(alpha, beta, s, depth - 1)[0])
            if v <= alpha:
                return v
            beta = min(beta, v)

        return v






            # That is the number in the corner is assigned the biggest weight.

    def score(self, grid):

        def calcScore(x, y):
            return x * pow(0.125, y)  # 0.125^y

        score1 = (
            calcScore(grid.map[0][0], 0) + calcScore(grid.map[0][1], 1) + calcScore(grid.map[0][2], 2)
            + calcScore(grid.map[0][3], 3) + calcScore(grid.map[1][3], 4) + calcScore(grid.map[1][2], 5)
            + calcScore(grid.map[1][1], 6) + calcScore(grid.map[1][0], 7) + calcScore(grid.map[2][0], 8)
            + calcScore(grid.map[2][1], 9) + calcScore(grid.map[2][2], 10) + calcScore(grid.map[2][3], 11)
            + calcScore(grid.map[3][3], 12) + calcScore(grid.map[3][2], 13) + calcScore(grid.map[3][1], 14)
            + calcScore(grid.map[3][0], 15))

        if grid.map[0][0] == grid.getMaxTile():  # award bonus for keeping max tile in corner
            score1 = 1.25 * score1

        emptyblock_score = len(grid.getAvailableCells())

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





import sys
import math
from BaseAI import BaseAI

MAX_VALUE = sys.maxint
MIN_VALUE = -MAX_VALUE
depth_limit = 4

class PlayerAI(BaseAI):


    def getMove(self, grid):
        return  self.alpha_beta_pruning(MIN_VALUE, MAX_VALUE, grid, depth_limit, 1)[1]




    def alpha_beta_pruning_player(self,alpha,beta,grid,depth,player):

        # 1 denote the player, 0 denotes the computer AI

        if depth == 0 or not grid.canMove():
            return [self.score(grid), None]

        if player==1:   ###### for user
            v=MIN_VALUE
            nextstates=[]
            nextmove = grid.getAvailableMoves()
            for action in nextmove:
                newGrid = grid.clone()
                newGrid.move(action)
                temp = [newGrid, action]  # stores each new state and the corresponding move
                nextstates.append(temp)

            for s in nextstates:
                vtmp = self.alpha_beta_pruning(alpha, beta,s[0], depth - 1,  0)


                if vtmp > v:
                    v = vtmp
                    bestMove = s[1]
                if v >= beta:
                    return [v, bestMove]

                alpha = max(alpha, v)

            return [v, bestMove]

        elif player==0:   ###### for Computer move

            v=MAX_VALUE
            nextstates=[]
            Emptycell = grid.getAvailableCells()

            for c in Emptycell:
                p,q=c
                newGrid=grid.clone()
                newGrid.map[p][q]=2
                nextstates.append(newGrid)
            for d in Emptycell:
                m,n=d
                newGrid=grid.clone()
                newGrid.map[m][n]=4
                nextstates.append(newGrid)

            for s in nextstates:
                v = min(v, self.alpha_beta_pruning(alpha, beta,s, depth - 1, 1)[0])
                if v <= alpha:
                    return v
                beta = min(beta, v)

            return v
        else:
            print "parameter error"


   #That is the number in the corner is assigned the biggest weight.
    def score(self,grid):


        def calcScore(x, y):
            return x * pow(0.125, y)  #0.125^y

        score1 = (
                    calcScore(grid.map[0][0], 0) + calcScore(grid.map[0][1], 1) + calcScore(grid.map[0][2], 2)
                  + calcScore(grid.map[0][3], 3) + calcScore(grid.map[1][3], 4) + calcScore(grid.map[1][2], 5)
                  + calcScore(grid.map[1][1], 6) + calcScore(grid.map[1][0], 7) + calcScore(grid.map[2][0], 8)
                  + calcScore(grid.map[2][1], 9) + calcScore(grid.map[2][2], 10) + calcScore(grid.map[2][3], 11)
                  + calcScore(grid.map[3][3], 12) + calcScore(grid.map[3][2], 13) + calcScore(grid.map[3][1], 14)
                  + calcScore(grid.map[3][0], 15))


        if grid.map[0][0] == grid.getMaxTile():  # award bonus for keeping max tile in corner
            score1 = 1.25 * score1

        emptyblock_score=len(grid.getAvailableCells())


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




