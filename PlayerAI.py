###############################################
# #!/usr/bin/env python
# #coding:utf-8
#jm4437  Jianpu Ma

################################################


import sys,os,math
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

        value = MIN_VALUE
        nextstates = []
        nextmove = grid.getAvailableMoves()
        for action in nextmove:
            newGrid = grid.clone()
            newGrid.move(action)
            moveset = [newGrid, action]  # stores each new state and the corresponding move
            nextstates.append(moveset)

        for movetuple in nextstates:
            nextgrid=movetuple[0]
            child = self.computer(alpha, beta, nextgrid, depth - 1)

            if child > value:
                value = child
                bestMove = movetuple[1]
            alpha = max(alpha, value)
            if beta <= alpha:
                return [value, bestMove]
        return [value, bestMove]

    def computer(self, alpha, beta, grid, depth):

        if depth == 0 or not grid.canMove():
            return [self.score(grid), None]

        value = MAX_VALUE
        nextstates = []
        Emptycell = grid.getAvailableCells()

        for x, y in Emptycell:
            newGrid = grid.clone()

            if randint(0,99) < 90: 
                newGrid.map[x][y] = 2
            else:
                newGrid.map[x][y] = 4 

            nextstates.append(newGrid)

        for x, y in Emptycell:
            newGrid = grid.clone()
            if randint(0,99) < 90: 
                newGrid.map[x][y] = 2
            else:
                newGrid.map[x][y] = 4 
            nextstates.append(newGrid)

        for s in nextstates:
            value = min(value, self.player(alpha, beta, s, depth - 1)[0])
            beta = min(beta, value)
            
            if beta <= alpha:
                return value        

        return value



   #That is the number in the corner is assigned the biggest weight.
    def score(self,grid):

    #########################################################################################################
    # Part I     The heuristic score for the empty tile, each weight 1
    ########################################################################################################
        emptyblock_score = len(grid.getAvailableCells())

    ##########################################################################################################
    # Part II     The heurisic score for the tortuous route, each weight according to the weight list by pow function
    #########################################################################################################

        weight = []
        for i in xrange(16):
            weight.append(pow(0.125, i))

        tortuous_order=[grid.map[0][0], grid.map[0][1], grid.map[0][2], grid.map[0][3],
                  grid.map[1][3], grid.map[1][2], grid.map[1][1], grid.map[1][0],
                  grid.map[2][0], grid.map[2][1], grid.map[2][2], grid.map[2][3],
                  grid.map[3][3], grid.map[3][2], grid.map[3][1], grid.map[3][0]]
        
        score1=0
        for i in xrange(16):
            
            score1+=tortuous_order[i]*weight[i]
        
        maxtile= grid.getMaxTile()

        if tortuous_order[0] == maxtile:  # award bonus for keeping max tile in corner  1.25
            score1 *= 1.25

        if tortuous_order[0] != maxtile: #penalty for moving max tile from corner   0.9
            score1 *= 0.95


    #####################################################################################
    # Part III     The smoothness score for the tortuous route
    #########################################################################################################
        """smoothness_score=0
        if tortuous_order[0] == maxtile:  
            for i in xrange(3):
                if tortuous_order[i+1]!=0:
                    if (tortuous_order[i]/tortuous_order[i+1]== 2 ):
                        smoothness_score+= 0.01"""



    #####################################################################################
    # total score
    #########################################################################################################
        score = score1 + emptyblock_score #+ smoothness_score

        return score











