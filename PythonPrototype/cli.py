#!/usr/bin/env python3.5
from rubic import Cube as RC
from solver import Solver

class Cli:
    _rc = RC()
    _continue = True

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

    def doCliThings():
        print("Hello! Welcome to Rushed Rubic's Cube!")
        while Cli._continue:
            print("Current cube:")
            Cli.display()
            Cli.chooseAction()

    def chooseAction():
        print("Please choose what to do next.")
        print("1. Randomize")
        print("2. Manual move")
        print("3. Explain possible moves")
        print("4. Solve the cube")
        print("5. Quit")
        choice = int(input("Choice: "))

        if choice == 1:
            Cli.randomize()
        elif choice == 2:
            Cli.chooseMove()
        elif choice == 3:
            Cli.explainMoves()
        elif choice == 4:
            pass
        elif choice == 5:
            Cli._continue = False

    def randomize():
        print("Please choose the number of random moves. Default 100.")
        moveCount = int(input("Move count: ") or "100")
        print("Randomizing..")
        Solver.randomize(Cli._rc, moveCount)

    def display():
        print(Cli._rc)


    def chooseMove():
        print("Please choose a move")
        Cli.listMoves()
        move = input("Your choice: ")
        move = Cli._moves[move]
        move(Cli._rc)

    def listMoves():
        print("Possible moves: " + str(Cli._moves.keys()))

    def explainMoves():
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

        
if __name__ == "__main__":
    Cli.doCliThings()
