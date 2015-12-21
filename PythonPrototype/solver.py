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
        print("Phase 1.")
        self.phase1()
        print("Phase 1 completed.")
        print(self._rc)
        print("Phase 2.")
        self.phase2()
        print("Phase 2 completed.")
        print(self._rc)
        print("Phase 3.")
        self.phase3()
        print("Phase 3 completed.")
        print(self._rc)
        print("Phase 4.")
        self.phase4()
        print("Phase 4 completed.")
        print(self._rc)
        print("Phase 5.")
        self.phase5()
        print("Phase 5 completed.")
        print(self._rc)
        print("Phase 6.")
        self.phase6()
        print("Phase 6 completed.")
        print(self._rc)
        print("Phase 7.")
        self.phase7()
        print("Phase 7 completed.")

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


    def phase1(self):
        rc = self._rc
        cornersFound = 1
        while cornersFound < 4:
            rc.y()
            position = self.lookForUCorner()
            if position == 0:
                cornersFound = cornersFound+1
            elif position == 1:
                Solver.p1a1(rc)
                cornersFound = cornersFound+1
            elif position == 2:
                Solver.p1a2(rc)
                cornersFound = cornersFound+1
            elif position == 3:
                Solver.p1a3(rc)
                cornersFound = cornersFound+1
            elif position == 4:
                Solver.p1a4(rc)
                cornersFound = cornersFound+1
            elif position == 5:
                Solver.p1a5(rc)
                cornersFound = cornersFound+1
            elif position == -1:
                if cornersFound == 1:
                    rc.y()
                    Solver.p1a1(rc)
                    rc.y()
                    Solver.p1a1(rc)
                    rc.yi()
                    rc.yi()
                    rc.yi()
                elif cornersFound == 2:
                    rc.y()
                    Solver.p1a1(rc)
                    rc.yi()
                    rc.yi()
                else: #Should be impossible
                    raise Exception

    def phase2(self):
        rc = self._rc
        sidesFound = 0
        while sidesFound != 4:
            position = self.lookForUSide()
            if position == 0:
                if Solver.checkIfP2Complete(rc):
                    return
            elif position == 1:
                Solver.p2a1(rc)
                sidesFound = sidesFound+1
            elif position == 2:
                Solver.p2a2(rc)
                sidesFound = sidesFound+1
            elif position == 3:
                Solver.p2a3(rc)
                sidesFound = sidesFound+1
            elif position == 4:
                Solver.p2a4(rc)
                sidesFound = sidesFound+1
            elif position == 5:
                Solver.p2a5(rc)
                sidesFound = sidesFound+1
            elif position == 6:
                Solver.p2a1(rc)
            elif position == -1:
                #Should be impossible
                raise Exception
            rc.y()


    def phase3(self):
        rc = self._rc
        Solver.rotateMiddle(rc)
        sidesFound = 0
        while sidesFound != 4:
            position = Solver.findMiddleLayerEdge(rc)
            if position == 0:
                return
            elif position == 1:
                Solver.p3a1(rc)
                sidesFound = sidesFound+1
            elif position == 2:
                Solver.p3a2(rc)
                sidesFound = sidesFound+1
            elif position == 3:
                Solver.p3a1(rc)
            elif position == 4:
                Solver.p3a2(rc)

    def phase4(self):
        rc = self._rc
        rc.x()
        rc.x()
        for i in range(2):
            position = Solver.whichToSwitch(rc)
            if position == 0:
                pass
            if position == 5 or position == 6:
                rc.y()
                Solver.p4a1(rc)
                rc.yi()
            if position == 1 or position == 5:
                Solver.p4a1(rc)
            if position == 2 or position == 6:
                Solver.p4a2(rc)
            if position == 3:
                Solver.p4a1(rc)
                Solver.p4a2(rc)
            rc.y()


    def phase5(self):
        rc = self._rc
        while not Solver.phase5Done(rc):
            moved = False
            for i in range(4):
                if Solver.hasPattern(rc):
                    Solver.p5a1(rc)
                    moved = True
                    break
                rc.y()
            if not moved:
                Solver.p5a1(rc)

    def phase6(self):
        rc = self._rc
        found = False
        while not found:
            for i in range(4):
                FColor = rc.F[1][1]
                if rc.F[1][0] == FColor or \
                   rc.U[1][2] == FColor:
                    found = True
                    break
                else:
                    rc.y()
            if not found:
                Solver.p6a1(rc)

        while not Solver.phase6Done(rc):
            Solver.p6a1(rc)


    def phase7(self):
        rc = self._rc
        for i in range(4):
            pattern = Solver.findPattern(rc)
            if pattern == "None":
                pass
            elif pattern == "H":
                Solver.p7a1(rc)
            elif pattern == "Fish":
                Solver.p7a2(rc)
            rc.y()
        

    def findPattern(rc):
        UColor = rc.U[1][1]
        if rc.U[0][1] != UColor and \
           rc.U[2][1] != UColor:
            return "H"
        elif rc.U[2][1] != UColor and \
             rc.U[1][2] != UColor:
            return "Fish"
        else:
            return "None"


    def phase6Done(rc):
        LColor = rc.L[1][1]
        RColor = rc.R[1][1]
        BColor = rc.B[1][1]
        if (rc.R[1][0] == RColor or \
           rc.U[2][1] == RColor) and \
           (rc.L[1][0] == LColor or \
           rc.U[0][1] == LColor)and \
           (rc.B[1][2] == BColor or \
           rc.U[1][0] == BColor):
            return True
        else:
            return False

    def phase5Done(rc):
        UColor = rc.U[1][1]
        if rc.U[0][0] == UColor and \
           rc.U[2][0] == UColor and \
           rc.U[2][2] == UColor and \
           rc.U[0][2] == UColor:
            return True
        else: 
            return False


    def hasPattern(rc):
        UColor = rc.U[1][1]
        if (rc.F[0][0] == UColor and \
           rc.U[2][2] == UColor) or \
           (rc.R[0][0] == UColor and \
           rc.R[2][0] == UColor) or \
           (rc.U[2][2] == UColor and \
           rc.R[2][0] == UColor):
            return True
        else:
            return False
        
            

    def whichToSwitch(rc):
        s24 = 0
        s12 = 0
        s34 = 0
        LColor = rc.L[1][1]
        if rc.L[2][0] != LColor and \
           rc.F[0][0] != LColor and \
           rc.U[0][2] != LColor:
            s12 = 1
        if rc.L[0][0] != LColor and \
           rc.B[0][2] != LColor and \
           rc.U[0][0] != LColor:
            s34 = 2
        if s12 == 1 and rc.R[0][0] != LColor and\
           rc.F[2][0] != LColor and \
           rc.U[2][2] != LColor:
            s24 = 4
        if s34 == 2 and rc.R[2][0] != LColor and\
           rc.B[2][2] != LColor and \
           rc.U[2][0] != LColor:
            s24 = 4
        return (s12 + s34 + s24)

    def rotateMiddle(rc):
        FColor = rc.F[0][0]
        for i in range(4):
            if rc.F[1][1] == FColor:
                return
            else:
                rc.rE()

    def findMiddleLayerEdge(rc):
        for j in range(4):
            rc.y()
            FColor = rc.F[0][0]
            LColor = rc.L[0][0]
            RColor = rc.R[0][0]
            for i in range(4):
                if rc.F[1][2] == FColor:
                    if rc.D[1][0] == LColor:
                        return 1
                    elif rc.D[1][0] == RColor:
                        return 2
                elif rc.F[0][1] == LColor and \
                     rc.L[2][1] == FColor:
                    return 3
                elif rc.F[2][1] == RColor and \
                     rc.R[0][1] == FColor:
                    return 4
                rc.rD()

        for i in range(4):
            if rc.D[1][0] == FColor:
                if rc.F[1][2] == LColor:
                    return 3
                elif rc.F[1][2] == RColor:
                    return 4
            rc.rD()
        
        #Is a cubicle stuck in middle layer?
        for i in range(4):
            FColor = rc.F[0][0]
            LColor = rc.L[0][0]
            RColor = rc.R[0][0]
            if rc.F[0][1] != FColor:
                return 3
            elif rc.F[2][1] != FColor:
                return 4
            rc.y()
        #Everything is already in place.
        return 0
            
    

    def checkIfP2Complete(rc):
        if rc.U[1][0] == rc.U[2][1] and \
           rc.U[2][1] == rc.U[1][2] and \
           rc.U[1][2] == rc.U[0][1]:
            return True
        return False    

    def lookForUSide(self):
        rc = self._rc
        UColor = rc.U[1][1]
        FColor = rc.F[0][0]
        for lookCount in range(4):
            if rc.U[1][2] == UColor and \
               rc.F[1][0] == FColor:
                return 0
            elif rc.D[1][0] == UColor and \
                 rc.F[1][2] == FColor:
                return 1
            elif rc.F[1][2] == UColor and \
                 rc.D[1][0] == FColor:
                return 2
            elif rc.R[0][1] == UColor and \
                 rc.F[2][1] == FColor:
                return 3
            elif rc.F[2][1] == UColor and \
                 rc.R[0][1] == FColor:
                return 4
            elif rc.F[1][0] == UColor and \
                 rc.U[1][2] == FColor:
                return 5
            rc.rDw()
        for lookCount in range(4):
            rc.y()
            if (rc.U[1][2] == UColor and \
               rc.F[1][0] == FColor) or \
               (rc.F[1][0] == UColor and \
               rc.U[1][2] == FColor):
                return 6
        return -1
            
        

    def checkIfDone(self):
        rc = self._rc
        return rc.U[0][0] == rc.U[2][0] and \
               rc.U[2][0] == rc.U[2][2] and \
               rc.U[2][2] == rc.U[0][2]

    def lookForUCorner(self):
        rc = self._rc
        UColor = rc.U[1][1]
        FColor = rc.F[0][0]
        for lookCount in range(4):
            if rc.U[2][2] == UColor and \
               rc.F[2][0] == FColor:
                return 0
            elif rc.R[0][2] == UColor and \
                 (rc.F[2][2] == FColor or \
                 rc.D[2][0] == FColor):
                return 1
            elif rc.F[2][2] == UColor and \
                 (rc.D[2][0] == FColor or \
                 rc.R[0][2] == FColor):
                return 2
            elif rc.D[2][0] == UColor and \
                 (rc.R[0][2] == FColor or \
                 rc.F[2][2] == FColor):
                return 3
            elif rc.F[2][0] == UColor and \
                 (rc.U[2][2] == FColor or \
                 rc.R[0][0] == FColor):
                return 4
            elif rc.R[0][0] == UColor and \
                 (rc.U[2][2] == FColor or \
                 rc.F[2][0] == FColor):
                return 5
            rc.rD()
        return -1



    def p1a1(rc):
        rc.rRi()
        rc.rDi()
        rc.rR()

    def p1a2(rc):
        rc.rDi()
        rc.rRi()
        rc.rD()
        rc.rR()

    def p1a3(rc):
        rc.rRi()
        rc.rD()
        rc.rR()
        rc.rD()
        rc.rD()
        rc.rRi()
        rc.rDi()
        rc.rR()

    def p1a4(rc):
        rc.rF()
        rc.rD()
        rc.rFi()
        rc.rD()
        rc.rD()
        rc.rRi()
        rc.rD()
        rc.rR()

    def p1a5(rc):
        rc.rRi()
        rc.rDi()
        rc.rR()
        rc.rD()
        rc.rRi()
        rc.rDi()
        rc.rR()

    def p2a1(rc):
        rc.rM()
        rc.rDi()
        rc.rDi()
        rc.rMi()

    def p2a2(rc):
        rc.rDi()
        rc.rM()
        rc.rD()
        rc.rMi()

    def p2a3(rc):
        rc.rE()
        rc.rF()
        rc.rEi()
        rc.rFi()

    def p2a4(rc):
        rc.rE()
        rc.rFi()
        rc.rEi()
        rc.rEi()
        rc.rF()

    def p2a5(rc):
        rc.rM()
        rc.rDi()
        rc.rDi()
        rc.rMi()
        rc.rDi()
        rc.rM()
        rc.rD()
        rc.rMi()

    def p3a1(rc):
        rc.rD()
        rc.rL()
        rc.rDi()
        rc.rLi()
        rc.rDi()
        rc.rFi()
        rc.rD()
        rc.rF()

    def p3a2(rc):
        rc.rDi()
        rc.rRi()
        rc.rD()
        rc.rR()
        rc.rD()
        rc.rF()
        rc.rDi()
        rc.rFi()

    def p4a1(rc):
        rc.rLi()
        rc.rUi()
        rc.rL()
        rc.rF()
        rc.rU()
        rc.rFi()
        rc.rLi()
        rc.rU()
        rc.rL()
        rc.rU()
        rc.rU()

    def p4a2(rc):
        rc.y()
        rc.rU()
        rc.rLi()
        rc.rUi()
        rc.rL()
        rc.rF()
        rc.rU()
        rc.rFi()
        rc.rLi()
        rc.rU()
        rc.rL()
        rc.rU()
        rc.yi()

    def p5a1(rc):
        rc.rLi()
        rc.rUi()
        rc.rL()
        rc.rUi()
        rc.rLi()
        rc.rUi()
        rc.rUi()
        rc.rL()
        rc.rUi()
        rc.rUi()

    def p6a1(rc):
        rc.rMi()
        rc.rUi()
        rc.rM()
        rc.rUi()
        rc.rUi()
        rc.rMi()
        rc.rUi()
        rc.rM()

    def p7a1(rc):
        rc.rRi()
        rc.rEi()
        rc.rRi()
        rc.rRi()
        rc.rEi()
        rc.rEi()
        rc.rRi()
        rc.rUi()
        rc.rUi()
        rc.rR()
        rc.rE()
        rc.rE()
        rc.rRi()
        rc.rRi()
        rc.rE()
        rc.rR()
        rc.rUi()
        rc.rUi()

    def p7a2(rc):
        rc.rFi()
        rc.rLi()
        rc.rRi()
        rc.rEi()
        rc.rRi()
        rc.rRi()
        rc.rEi()
        rc.rEi()
        rc.rRi()
        rc.rUi()
        rc.rUi()
        rc.rR()
        rc.rE()
        rc.rE()
        rc.rRi()
        rc.rRi()
        rc.rE()
        rc.rR()
        rc.rUi()
        rc.rUi()
        rc.rL()
        rc.rF()
