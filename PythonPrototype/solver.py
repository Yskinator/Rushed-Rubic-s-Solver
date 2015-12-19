from rubic import Cube as RC
import random

class Solver:
    _moves = [RC.rF, RC.rFi, RC.rFw, RC.rFiw, \
              RC.rL, RC.rLi, RC.rLw, RC.rLiw, \
              RC.rR, RC.rRi, RC.rRw, RC.rRiw, \
              RC.rU, RC.rUi, RC.rUw, RC.rUiw, \
              RC.rD, RC.rDi, RC.rDw, RC.rDiw, \
              RC.rB, RC.rBi, RC.rBw, RC.rBiw]
        

    def randomize(rc, moveCount):
        for i in range(moveCount):
            move = random.choice(Solver._moves)
            move(rc)


