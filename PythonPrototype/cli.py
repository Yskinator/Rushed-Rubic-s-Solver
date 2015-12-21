#!/usr/bin/env python3.5
from rubic import Cube as RC
from solver import Solver
import time

class Cli:
    _rc = False
    _solver = False
    _continue = True
    _waitTime = 0.1
    _moveCount = 0

    _moves = {"F": RC.rF, "Fi": RC.rFi, \
              "Fw": RC.rFw, "Fiw": RC.rFiw, \
              "L": RC.rL, "Li": RC.rLi, \
              "Lw": RC.rLw, "Liw": RC.rLiw, \
              "R": RC.rR, "Ri": RC.rRi, \
              "Rw": RC.rRw, "Riw": RC.rRiw, \
              "U": RC.rU, "Ui": RC.rUi, \
              "Uw": RC.rUw, "Uiw": RC.rUiw, \
              "D": RC.rD, "Di": RC.rDi, \
              "Dw": RC.rDw, "Diw": RC.rDiw, \
              "B": RC.rB, "Bi": RC.rBi, \
              "Bw": RC.rBw, "Biw": RC.rBiw, \
              "E": RC.rE, "Ei": RC.rEi, \
              "M": RC.rM, "Mi": RC.rMi, \
              "S": RC.rS, "Si": RC.rSi, \
              "x": RC.x, "y": RC.y, "z": RC.z, \
              "xi": RC.xi, "yi": RC.yi, \
              "zi": RC.zi}

    def __init__(self):
        self._rc = RC()
        self._solver = Solver(self._rc, self)

    def doCliThings(self):
        print("Hello! Welcome to Rushed Rubic's Cube!")
        while cli._continue:
            print("Current cube:")
            cli.display()
            cli.chooseAction()

    def chooseAction(self):
        print("Please choose what to do next.")
        print("1. Randomize")
        print("2. Manual move")
        print("3. Explain possible moves")
        print("4. Solve the cube")
        print("5. Set move delay")
        print("6. Quit")
        choice = input("Choice: ")

        if choice == "1":
            cli.randomize()
        elif choice == "2":
            cli.chooseMove()
        elif choice == "3":
            cli.explainMoves()
        elif choice == "4":
            cli.solve()
        elif choice == "5":
            cli.setDelay()
        elif choice == "6":
            cli._continue = False
        else:
            print("Please enter a valid number.")

    def setDelay(self):
        delay = input("Delay in seconds: ")
        try:
            delay = float(delay)
            self._waitTime = delay
        except ValueError:
            print("Invalid value. No changes.")

    def randomize(self):
        print("Please choose the number of random moves. Default 100.")
        moveCount = input("Move count: ") or "100"
        try:
            moveCount = int(moveCount)
        except ValueError:
            moveCount = 100

        print("Randomizing..")
        self._solver.randomize(moveCount)

    def display(self):
        print(cli._rc)


    def chooseMove(self):
        print("Please choose a move")
        cli.listMoves()
        move = input("Your choice: ")
        cli.execute(move)

    def execute(self, move):
        try:
            move = cli._moves[move]
            move(cli._rc)
            self._moveCount = self._moveCount+1
        except KeyError:
            print("Invalid move.")

    def do(self,move):
        print("Executing move " + move)
        self.execute(move)
        print("Current status:")
        print(self._rc)
        time.sleep(self._waitTime)

    def show(self, message):
        print(message)

    def listMoves(self):
        print("Possible moves: " + str(cli._moves.keys()))

    def explainMoves(self):
        print("The cube has six faces.")
        print("Front, left, right, up, down,  behind.")
        print("We refer to these as F, L, R, U, D and B.")
        print("It also has the following:")
        print("Middle, M - the layer between L and R.")
        print("Equator, E - between U and D")
        print("Standing, S - betwen F and B")
        print("\n")
        print("Possible moves are as follows:")
        print("Rotate one of the faces, for instance F or L.")
        print("By default, rotates a single layer clockwise.")
        print("Suffix -i inverts the rotation.")
        print("Suffix -w rotates two layers.")
        print("When using both, i comes first. For instance, Uiw or Liw.")
        print("")
        print("M, E and S can also be rotated.")
        print("Rotation directions:")
        print("M: same as L, E: D and S: F")
        print("")
        print("Finally, the entire cube can be rotated around its x, y or z axis.")
        print("x is like a hypotetical Rww rotation.")
        print("y is like 'Uww', z is like 'Fww'.")


    def solve(self):
        self._moveCount = 0
        self._solver.solve(cli._rc, self)
        print("Total moves: " + str(self._moveCount))

        
if __name__ == "__main__":
    cli = Cli()
    cli.doCliThings()
