
class Cube:
    F = [["R" for x in range(3)] for y in range(3)]
    L = [["Y" for x in range(3)] for y in range(3)]
    R = [["W" for x in range(3)] for y in range(3)]
    U = [["G" for x in range(3)] for y in range(3)]
    D = [["B" for x in range(3)] for y in range(3)]
    B = [["O" for x in range(3)] for y in range(3)]


    def __str__(self):
        indentation = "       "
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


    def setSide(self, sideName, side):
        if sideName == "F":
            self.F = side
        elif sideName == "L":
            self.L = side
        elif sideName == "R":
            self.R = side
        elif sideName == "U":
            self.U = side
        elif sideName == "D":
            self.D = side
        elif sideName == "B":
            self.B = side


    #Rotates a face of the cube - and only
    #the face! - 90 degrees clockwise.
    def rFace(face):
        newFace = [["" for x in range(3)] for y in range(3)]
        for y in range(3):
            for x in range(3):
                newFace[x][y] = face[y][2-x]
        return newFace


    #Inverts face's y-axis
    def iFaceY(face):
        return [[face[x][2-y] for y in range(3)] for x in range(3)]


    #Inverts face's x-axis
    def iFaceX(face):
        return [[face[2-x][y] for y in range(3)] for x in range(3)]
  

    #Rotates a face of the cube - and only
    #the face! - 90 degrees counter-clockwise
    def rFacei(face):
        newFace = Cube.rFace(face)
        newFace = Cube.rFace(newFace)
        newFace = Cube.rFace(newFace)
        return newFace


    #Rotates the entire cube clockwise on R
    def x(self):
        self.R = Cube.rFace(self.R)
        self.L = Cube.rFacei(self.L)
        temp = self.U
        self.U = self.F
        self.F = self.D
        self.D = self.B
        self.B = temp


    #Rotates the entire cube counter-clockwise on R
    def xi(self):
        self.x()
        self.x()
        self.x()


    #Rotates the entire cube clockwise on U
    def y(self):
        self.U = Cube.rFace(self.U)
        self.D = Cube.rFacei(self.D)
        temp = Cube.iFaceX(Cube.iFaceY(self.L))
        self.L = self.F
        self.F = self.R
        self.R = Cube.iFaceX(Cube.iFaceY(self.B))
        self.B = temp


    #Rotates the entire cube counter-clockwise on U
    def yi(self):
        self.y()
        self.y()
        self.y()


    #Rotates the entire cube clockwise on F
    def z(self):
        self.F = Cube.rFace(self.F)
        self.B = Cube.rFacei(self.B)
        temp = Cube.rFace(self.U)
        self.U = Cube.rFace(self.L)
        self.L = Cube.rFace(self.D)
        self.D = Cube.rFace(self.R)
        self.R = temp

    def zi(self):
        self.z()
        self.z()
        self.z()


    #Without i: clockwise
    #With i: counter-clockwise
    #Without w: only one layer
    #With w: also the corresponding middle layer

    def rF(self):
        self.F = Cube.rFace(self.F)

        temp = [self.U[x][2] for x in range(3)]
        for x in range(3):
            self.U[x][2] = self.L[2][2-x]
        for y in range(3):
            self.L[2][y] = self.D[y][0]
        for x in range(3):
            self.D[x][0] = self.R[0][2-x]
        for y in range(3):
            self.R[0][y] = temp[y]



    def rFi(self):
        self.rF()
        self.rF()
        self.rF()


    def rFw(self):
        self.rF()

        temp = [self.U[x][1] for x in range(3)]
        for x in range(3):
            self.U[x][1] = self.L[1][2-x]
        for y in range(3):
            self.L[1][y] = self.D[y][1]
        for x in range(3):
            self.D[x][1] = self.R[1][2-x]
        for y in range(3):
            self.R[1][y] = temp[y]
        

    def rFiw(self):
        self.rFw()
        self.rFw()
        self.rFw()


    def rL(self):
        self.yi()
        self.rF()
        self.y()


    def rLi(self):
        self.yi()
        self.rFi()
        self.y()

    def rLw(self):
        self.yi()
        self.rFw()
        self.y()

    def rLiw(self):
        self.yi()
        self.rFiw()
        self.y()

    def rR(self):
        self.y()
        self.rF()
        self.yi()

    def rRi(self):
        self.y()
        self.rFi()
        self.yi()

    def rRw(self):
        self.y()
        self.rFw()
        self.yi()

    def rRiw(self):
        self.y()
        self.rFiw()
        self.yi()

    def rU(self):
        self.xi()
        self.rF()
        self.x()

    def rUi(self):
        self.xi()
        self.rFi()
        self.x()

    def rUw(self):
        self.xi()
        self.rFw()
        self.x()

    def rUiw(self):
        self.xi()
        self.rFiw()
        self.x()

    def rD(self):
        self.x()
        self.rF()
        self.xi()

    def rDi(self):
        self.x()
        self.rFi()
        self.xi()

    def rDw(self):
        self.x()
        self.rFw()
        self.xi()

    def rDiw(self):
        self.x()
        self.rFiw()
        self.xi()

    def rB(self):
        self.y()
        self.y()
        self.rF()
        self.y()
        self.y()

    def rBi(self):
        self.y()
        self.y()
        self.rFi()
        self.y()
        self.y()

    def rBw(self):
        self.y()
        self.y()
        self.rFw()
        self.y()
        self.y()

    def rBiw(self):
        self.y()
        self.y()
        self.rFiw()
        self.y()
        self.y()

    #E or equator is the layer between U and D
    #Turn direction same as D
    def rE(self):
        self.rDw()
        self.rDi()

    def rEi(self):
        self.rDiw()
        self.rD()

    #M or middle is the layer between L and R
    #Turn direction same as L
    def rM(self):
        self.rLw()
        self.rLi()

    def rMi(self):
        self.rLiw()
        self.rL()

    #S or standing is the layer between F and B
    #Turn direction same as F
    def rS(self):
        self.rFw()
        self.rFi()

    def rSi(self):
        self.rFiw()
        self.rF()

