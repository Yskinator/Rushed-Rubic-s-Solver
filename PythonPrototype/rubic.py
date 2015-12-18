#!/usr/bin/env python3.5

class Rubic:
    F = [[""+str(x)+str(y) for x in range(3)] for y in range(3)]
    L = [[1 for x in range(3)] for y in range(3)]
    R = [[2 for x in range(3)] for y in range(3)]
    U = [[3 for x in range(3)] for y in range(3)]
    D = [[4 for x in range(3)] for y in range(3)]
    B = [[5 for x in range(3)] for y in range(3)]

    #Capital letter means clockwise rotation
    #Two letters mean the first two layers
    def dF(self):
        nF = [["" for x in range(3)] for y in range(3)]
        for y in range(3):
            for x in range(3):
                nF[x][y] = self.F[2-y][x]
        self.F = nF

        

