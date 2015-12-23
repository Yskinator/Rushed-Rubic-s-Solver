from rubic import Cube as RC
import random

class Solver:
    _ui = False
    _rc = False
    _moves = ["F", "Fi", "Fw", "Fiw", \
              "L", "Li", "Lw", "Liw", \
              "R", "Ri", "Rw", "Riw", \
              "U", "Ui", "Uw", "Uiw", \
              "D", "Di", "Dw", "Diw", \
              "B", "Bi", "Bw", "Biw", \
              "E", "Ei", "M", "Mi", \
              "S", "Si"]
        

    def __init__(self, rc, ui):
        self._rc = rc
        self._ui = ui

    def randomize(self, moveCount, show = False):
        for i in range(moveCount):
            move = random.choice(self._moves)
            if show:
                self._ui.do(move)
            else: 
                self._ui.execute(move)


    def solve(self, rc, ui):
        self._rc = rc
        self._ui = ui
        self._ui.show("Priming cube.")
        self.primeCube()
        self._ui.show("Primed.")
        self._ui.show(self._rc)
        self._ui.show("Phase 1.")
        self.phase1()
        self._ui.show("Phase 1 completed.")
        self._ui.show(self._rc)
        self._ui.show("Phase 2.")
        self.phase2()
        self._ui.show("Phase 2 completed.")
        self._ui.show(self._rc)
        self._ui.show("Phase 3.")
        self.phase3()
        self._ui.show("Phase 3 completed.")
        self._ui.show(self._rc)
        self._ui.show("Phase 4.")
        self.phase4()
        self._ui.show("Phase 4 completed.")
        self._ui.show(self._rc)
        self._ui.show("Phase 5.")
        self.phase5()
        self._ui.show("Phase 5 completed.")
        self._ui.show(self._rc)
        self._ui.show("Phase 6.")
        self.phase6()
        self._ui.show("Phase 6 completed.")
        self._ui.show(self._rc)
        self._ui.show("Phase 7.")
        self.phase7()
        self._ui.show("Phase 7 completed.")

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
        self.randomize(self._rc, 10, True)
        self.primeCube()
        return

    #Is one of U's corners the same color as its
    #center?
    def UCorner(self):
        rc = self._rc
        color = rc.U[1][1]
        if rc.U[2][2] == color:
            return True
        elif rc.U[0][2] == color:
            self._ui.do("yi")
            return True
        elif rc.U[2][0] == color:
            self._ui.do("y")
            return True
        elif rc.U[0][0] == color:
            self._ui.do("y")
            self._ui.do("y")
            return True
        else:
            return False

    #Is one of F's corners the same color as its
    #center?
    def FCorner(self):
        rc = self._rc
        color = rc.F[1][1]
        if rc.F[2][2] == color:
            self._ui.do("x")
            return True
        elif rc.F[2][0] == color:
            self._ui.do("z")
            self._ui.do("x")
            return True
        elif rc.F[0][2] == color:
            self._ui.do("zi")
            self._ui.do("x")
            return True
        elif rc.F[0][0] == color:
            self._ui.do("z")
            self._ui.do("z")
            self._ui.do("x")
            return True
        else:
            return False

    def LCorner(self):
        rc = self._rc
        color = rc.L[1][1]
        if rc.L[2][0] == color:
            self._ui.do("z")
            return True
        elif rc.L[0][0] == color:
            self._ui.do("xi")
            self._ui.do("z")
            return True
        elif rc.L[2][2] == color:
            self._ui.do("x")
            self._ui.do("z")
            return True
        elif rc.L[0][2] == color:
            self._ui.do("x")
            self._ui.do("x")
            self._ui.do("z")
            return True
        else:
            return False

    def RCorner(self):
        rc = self._rc
        color = rc.R[1][1]
        if rc.R[0][2] == color:
            self._ui.do("zi")
            return True
        elif rc.R[2][2] == color:
            self._ui.do("x")
            self._ui.do("zi")
            return True
        elif rc.R[0][0] == color:
            self._ui.do("xi")
            self._ui.do("zi")
            return True
        elif rc.R[2][0] == color:
            self._ui.do("x")
            self._ui.do("x")
            self._ui.do("zi")
            return True
        else:
            return False


    def BCorner(self):
        rc = self._rc
        color = rc.B[1][1]
        if rc.B[2][2] == color:
            self._ui.do("xi")
            return True
        elif rc.B[2][0] == color:
            self._ui.do("zi")
            self._ui.do("xi")
            return True
        elif rc.B[0][2] == color:
            self._ui.do("z")
            self._ui.do("xi")
            return True
        elif rc.B[0][0] == color:
            self._ui.do("z")
            self._ui.do("z")
            self._ui.do("xi")
            return True
        else:
            return False


    def DCorner(self):
        rc = self._rc
        color = rc.D[1][1]
        if rc.D[2][2] == color:
            self._ui.do("x")
            self._ui.do("x")
            return True
        elif rc.D[2][0] == color:
            self._ui.do("yi")
            self._ui.do("x")
            self._ui.do("x")
            return True
        elif rc.D[0][2] == color:
            self._ui.do("y")
            self._ui.do("x")
            self._ui.do("x")
            return True
        elif rc.D[0][0] == color:
            self._ui.do("y")
            self._ui.do("y")
            self._ui.do("x")
            self._ui.do("x")
            return True
        else:
            return False


    def phase1(self):
        rc = self._rc
        cornersFound = 1
        while cornersFound < 4:
            self._ui.do("y")
            position = self.lookForUCorner()
            if position == 0:
                cornersFound = cornersFound+1
            elif position == 1:
                self.p1a1()
                cornersFound = cornersFound+1
            elif position == 2:
                self.p1a2()
                cornersFound = cornersFound+1
            elif position == 3:
                self.p1a3()
                cornersFound = cornersFound+1
            elif position == 4:
                self.p1a4()
                cornersFound = cornersFound+1
            elif position == 5:
                self.p1a5()
                cornersFound = cornersFound+1
            elif position == -1:
                if cornersFound == 1:
                    self._ui.do("y")
                    self.p1a1()
                    self._ui.do("y")
                    self.p1a1()
                    self._ui.do("yi")
                    self._ui.do("yi")
                    self._ui.do("yi")
                elif cornersFound == 2:
                    self._ui.do("y")
                    self.p1a1()
                    self._ui.do("yi")
                    self._ui.do("yi")
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
                self.p2a1()
                sidesFound = sidesFound+1
            elif position == 2:
                self.p2a2()
                sidesFound = sidesFound+1
            elif position == 3:
                self.p2a3()
                sidesFound = sidesFound+1
            elif position == 4:
                self.p2a4()
                sidesFound = sidesFound+1
            elif position == 5:
                self.p2a5()
                sidesFound = sidesFound+1
            elif position == 6:
                self.p2a1()
            elif position == -1:
                #Should be impossible
                raise Exception
            self._ui.do("y")


    def phase3(self):
        rc = self._rc
        self.rotateMiddle()
        sidesFound = 0
        while sidesFound != 4:
            position = self.findMiddleLayerEdge()
            if position == 0:
                return
            elif position == 1:
                self.p3a1()
                sidesFound = sidesFound+1
            elif position == 2:
                self.p3a2()
                sidesFound = sidesFound+1
            elif position == 3:
                self.p3a1()
            elif position == 4:
                self.p3a2()

    def phase4(self):
        rc = self._rc
        self._ui.do("x")
        self._ui.do("x")
        for i in range(2):
            position = Solver.whichToSwitch(rc)
            if position == 0:
                pass
            if position == 5 or position == 6:
                self._ui.do("y")
                self.p4a1()
                self._ui.do("yi")
            if position == 1 or position == 5:
                self.p4a1()
            if position == 2 or position == 6:
                self.p4a2()
            if position == 3:
                self.p4a1()
                self.p4a2()
            self._ui.do("y")


    def phase5(self):
        rc = self._rc
        while not Solver.phase5Done(rc):
            moved = False
            for i in range(4):
                if Solver.hasPattern(rc):
                    self.p5a1()
                    moved = True
                    break
                self._ui.do("y")
            if not moved:
                self.p5a1()

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
                    self._ui.do("y")
            if not found:
                self.p6a1()

        while not Solver.phase6Done(rc):
            self.p6a1()


    def phase7(self):
        rc = self._rc
        for i in range(4):
            pattern = Solver.findPattern(rc)
            if pattern == "None":
                pass
            elif pattern == "H":
                self.p7a1()
            elif pattern == "Fish":
                self.p7a2()
            self._ui.do("y")
        

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

    def rotateMiddle(self):
        FColor = self._rc.F[0][0]
        for i in range(4):
            if self._rc.F[1][1] == FColor:
                return
            else:
                self._ui.do("E")

    def findMiddleLayerEdge(self):
        rc = self._rc
        for j in range(4):
            self._ui.do("y")
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
                self._ui.do("D")

        for i in range(4):
            if rc.D[1][0] == FColor:
                if rc.F[1][2] == LColor:
                    return 3
                elif rc.F[1][2] == RColor:
                    return 4
            self._ui.do("D")
        
        #Is a cubicle stuck in middle layer?
        for i in range(4):
            FColor = rc.F[0][0]
            LColor = rc.L[0][0]
            RColor = rc.R[0][0]
            if rc.F[0][1] != FColor:
                return 3
            elif rc.F[2][1] != FColor:
                return 4
            self._ui.do("y")
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
            self._ui.do("Dw")
        for lookCount in range(4):
            self._ui.do("y")
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
            self._ui.do("D")
        return -1



    def p1a1(self):
        self._ui.do("Ri")
        self._ui.do("Di")
        self._ui.do("R")

    def p1a2(self):
        self._ui.do("Di")
        self._ui.do("Ri")
        self._ui.do("D")
        self._ui.do("R")

    def p1a3(self):
        self._ui.do("Ri")
        self._ui.do("D")
        self._ui.do("R")
        self._ui.do("D")
        self._ui.do("D")
        self._ui.do("Ri")
        self._ui.do("Di")
        self._ui.do("R")

    def p1a4(self):
        self._ui.do("F")
        self._ui.do("D")
        self._ui.do("Fi")
        self._ui.do("D")
        self._ui.do("D")
        self._ui.do("Ri")
        self._ui.do("D")
        self._ui.do("R")

    def p1a5(self):
        self._ui.do("Ri")
        self._ui.do("Di")
        self._ui.do("R")
        self._ui.do("D")
        self._ui.do("Ri")
        self._ui.do("Di")
        self._ui.do("R")

    def p2a1(self):
        self._ui.do("M")
        self._ui.do("Di")
        self._ui.do("Di")
        self._ui.do("Mi")

    def p2a2(self):
        self._ui.do("Di")
        self._ui.do("M")
        self._ui.do("D")
        self._ui.do("Mi")

    def p2a3(self):
        self._ui.do("E")
        self._ui.do("F")
        self._ui.do("Ei")
        self._ui.do("Fi")

    def p2a4(self):
        self._ui.do("E")
        self._ui.do("Fi")
        self._ui.do("Ei")
        self._ui.do("Ei")
        self._ui.do("F")

    def p2a5(self):
        self._ui.do("M")
        self._ui.do("Di")
        self._ui.do("Di")
        self._ui.do("Mi")
        self._ui.do("Di")
        self._ui.do("M")
        self._ui.do("D")
        self._ui.do("Mi")

    def p3a1(self):
        self._ui.do("D")
        self._ui.do("L")
        self._ui.do("Di")
        self._ui.do("Li")
        self._ui.do("Di")
        self._ui.do("Fi")
        self._ui.do("D")
        self._ui.do("F")

    def p3a2(self):
        self._ui.do("Di")
        self._ui.do("Ri")
        self._ui.do("D")
        self._ui.do("R")
        self._ui.do("D")
        self._ui.do("F")
        self._ui.do("Di")
        self._ui.do("Fi")

    def p4a1(self):
        self._ui.do("Li")
        self._ui.do("Ui")
        self._ui.do("L")
        self._ui.do("F")
        self._ui.do("U")
        self._ui.do("Fi")
        self._ui.do("Li")
        self._ui.do("U")
        self._ui.do("L")
        self._ui.do("U")
        self._ui.do("U")

    def p4a2(self):
        self._ui.do("y")
        self._ui.do("U")
        self._ui.do("Li")
        self._ui.do("Ui")
        self._ui.do("L")
        self._ui.do("F")
        self._ui.do("U")
        self._ui.do("Fi")
        self._ui.do("Li")
        self._ui.do("U")
        self._ui.do("L")
        self._ui.do("U")
        self._ui.do("yi")

    def p5a1(self):
        self._ui.do("Li")
        self._ui.do("Ui")
        self._ui.do("L")
        self._ui.do("Ui")
        self._ui.do("Li")
        self._ui.do("Ui")
        self._ui.do("Ui")
        self._ui.do("L")
        self._ui.do("Ui")
        self._ui.do("Ui")

    def p6a1(self):
        self._ui.do("Mi")
        self._ui.do("Ui")
        self._ui.do("M")
        self._ui.do("Ui")
        self._ui.do("Ui")
        self._ui.do("Mi")
        self._ui.do("Ui")
        self._ui.do("M")

    def p7a1(self):
        self._ui.do("Ri")
        self._ui.do("Ei")
        self._ui.do("Ri")
        self._ui.do("Ri")
        self._ui.do("Ei")
        self._ui.do("Ei")
        self._ui.do("Ri")
        self._ui.do("Ui")
        self._ui.do("Ui")
        self._ui.do("R")
        self._ui.do("E")
        self._ui.do("E")
        self._ui.do("Ri")
        self._ui.do("Ri")
        self._ui.do("E")
        self._ui.do("R")
        self._ui.do("Ui")
        self._ui.do("Ui")

    def p7a2(self):
        self._ui.do("Fi")
        self._ui.do("Li")
        self._ui.do("Ri")
        self._ui.do("Ei")
        self._ui.do("Ri")
        self._ui.do("Ri")
        self._ui.do("Ei")
        self._ui.do("Ei")
        self._ui.do("Ri")
        self._ui.do("Ui")
        self._ui.do("Ui")
        self._ui.do("R")
        self._ui.do("E")
        self._ui.do("E")
        self._ui.do("Ri")
        self._ui.do("Ri")
        self._ui.do("E")
        self._ui.do("R")
        self._ui.do("Ui")
        self._ui.do("Ui")
        self._ui.do("L")
        self._ui.do("F")
