#!/usr/bin/env python3.5

class Rubic:
    F = [["F"+str(x)+str(y) for x in range(3)] for y in range(3)]
    L = [["L"+str(x)+str(y) for x in range(3)] for y in range(3)]
    R = [["R"+str(x)+str(y) for x in range(3)] for y in range(3)]
    U = [["U"+str(x)+str(y) for x in range(3)] for y in range(3)]
    D = [["D"+str(x)+str(y) for x in range(3)] for y in range(3)]
    B = [["B"+str(x)+str(y) for x in range(3)] for y in range(3)]

    def __str__(self):
        indentation = "             "
        s = ""
        for y in range(3):
            s = s + indentation
            for x in range(3):
                s = s + str(self.U[x][y]) + " "
            s = s + "\n"
        s = s + "\n"

        for y in range(3):
            for x in range(3):
                s = s + str(self.L[x][y]) + " "
            s = s + " "
            for x in range(3):
                s = s + str(self.F[x][y]) + " "
            s = s + " "
            for x in range(3):
                s = s + str(self.R[x][y]) + " "
            s = s + "\n"
        s = s + "\n"

        for y in range(3):
            s = s + indentation
            for x in range(3):
                s = s + str(self.D[x][y]) + " "
            s = s + "\n"
        s = s + "\n"

        for y in range(3):
            s = s + indentation
            for x in range(3):
                s = s + str(self.B[x][y]) + " "
            s = s + "\n"

        return s

    #Without i: clockwise
    #With i: counter-clockwise
    #Without w: only one layer
    #With w: also the corresponding middle layer

    def tF(self):
        newF = [["" for x in range(3)] for y in range(3)]
        for y in range(3):
            for x in range(3):
                newF[x][y] = self.F[y][2-x]
        self.F = newF

        temp = [self.U[x][2] for x in range(3)]
        for x in range(3):
            self.U[x][2] = self.L[2][2-x]
        for y in range(3):
            self.L[2][y] = self.D[y][0]
        for x in range(3):
            self.D[x][0] = self.R[0][2-x]
        for y in range(3):
            self.R[0][y] = temp[y]



    def tFi(self):
        newF = [["" for x in range(3)] for y in range(3)]
        for y in range(3):
            for x in range(3):
                newF[x][y] = self.F[2-y][x]
        self.F = newF
        
        temp = [self.U[x][2] for x in range(3)]
        for x in range(3):
            self.U[x][2] = self.R[0][x]
        for y in range(3):
            self.R[0][y] = self.D[2-y][0]
        for x in range(3):
            self.D[x][0] = self.L[2][x]
        for y in range(3):
            self.L[2][y] = temp[2-y]




r = Rubic()
print(r)
print("\n\n")
r.tFi()
print(r)        

