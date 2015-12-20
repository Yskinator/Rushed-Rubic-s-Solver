from rubic import Cube as RC
import random

class Solver:
    _rc = False
    _moves = [RC.rF, RC.rFi, RC.rFw, RC.rFiw, \
              RC.rL, RC.rLi, RC.rLw, RC.rLiw, \
              RC.rR, RC.rRi, RC.rRw, RC.rRiw, \
              RC.rU, RC.rUi, RC.rUw, RC.rUiw, \
              RC.rD, RC.rDi, RC.rDw, RC.rDiw, \
              RC.rB, RC.rBi, RC.rBw, RC.rBiw, \
              RC.rE, RC.rEi, RC.rM, RC.rMi, \
              RC.rS, RC.rSi]
        

    def randomize(rc, moveCount):
        for i in range(moveCount):
            move = random.choice(Solver._moves)
            move(rc)


    def solve(self,rc):
        self._rc = rc
        print("Priming cube.")
        self.primeCube()
        print("Primed.")
        print(self._rc)

    #Pick a corner that's the same color as the
    #center of the face it is on. Rotate cube so
    #that it is the bottom right corner of U.
    def primeCube(self):
        if self.UCorner():
            return
        elif self.FCorner():
            return
        elif self.LCorner():
            return
        elif self.RCorner():
            return
        elif self.BCorner():
            return
        elif self.DCorner():
            return
        Solver.randomize(self._rc,10)
        self.primeCube()
        return

    #Is one of U's corners the same color as its
    #center?
    def UCorner(self):
        _rc = self._rc
        color = _rc.U[1][1]
        if _rc.U[2][2] == color:
            return True
        elif _rc.U[0][2] == color:
            _rc.yi()
            return True
        elif _rc.U[2][0] == color:
            _rc.y()
            return True
        elif _rc.U[0][0] == color:
            _rc.y()
            _rc.y()
            return True
        else:
            return False

    #Is one of F's corners the same color as its
    #center?
    def FCorner(self):
        _rc = self._rc
        color = _rc.F[1][1]
        if _rc.F[2][2] == color:
            _rc.x()
            return True
        elif _rc.F[2][0] == color:
            _rc.z()
            _rc.x()
            return True
        elif _rc.F[0][2] == color:
            _rc.zi()
            _rc.x()
            return True
        elif _rc.F[0][0] == color:
            _rc.z()
            _rc.z()
            _rc.x()
            return True
        else:
            return False

    def LCorner(self):
        _rc = self._rc
        color = _rc.L[1][1]
        if _rc.L[2][0] == color:
            _rc.z()
            return True
        elif _rc.L[0][0] == color:
            _rc.xi()
            _rc.z()
            return True
        elif _rc.L[2][2] == color:
            _rc.x()
            _rc.z()
            return True
        elif _rc.L[0][2] == color:
            _rc.x()
            _rc.x()
            _rc.z()
            return True
        else:
            return False

    def RCorner(self):
        _rc = self._rc
        color = _rc.R[1][1]
        if _rc.R[0][2] == color:
            _rc.zi()
            return True
        elif _rc.R[2][2] == color:
            _rc.x()
            _rc.zi()
            return True
        elif _rc.R[0][0] == color:
            _rc.xi()
            _rc.zi()
            return True
        elif _rc.R[2][0] == color:
            _rc.x()
            _rc.x()
            _rc.zi()
            return True
        else:
            return False


    def BCorner(self):
        _rc = self._rc
        color = _rc.B[1][1]
        if _rc.B[2][2] == color:
            _rc.xi()
            return True
        elif _rc.B[2][0] == color:
            _rc.zi()
            _rc.xi()
            return True
        elif _rc.B[0][2] == color:
            _rc.z()
            _rc.xi()
            return True
        elif _rc.B[0][0] == color:
            _rc.z()
            _rc.z()
            _rc.xi()
            return True
        else:
            return False


    def DCorner(self):
        _rc = self._rc
        color = _rc.D[1][1]
        if _rc.D[2][2] == color:
            _rc.x()
            _rc.x()
            return True
        elif _rc.D[2][0] == color:
            _rc.yi()
            _rc.x()
            _rc.x()
            return True
        elif _rc.D[0][2] == color:
            _rc.y()
            _rc.x()
            _rc.x()
            return True
        elif _rc.D[0][0] == color:
            _rc.y()
            _rc.y()
            _rc.x()
            _rc.x()
            return True
        else:
            return False
