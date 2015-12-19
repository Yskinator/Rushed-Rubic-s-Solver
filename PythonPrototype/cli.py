#!/usr/bin/env python3.5
from rubic import Cube as RubicCube
from solver import Solver

class Cli:
    _rc = RubicCube()
    _continue = True
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
        print("3. Solve")
        print("4. Quit")
        choice = int(input("Choice: "))

        if choice == 1:
            Cli.randomize()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            Cli._continue = False

    def randomize():
        print("Please choose the number of random moves. Default 100.")
        moveCount = int(input("Move count: ") or "100")
        print("Randomizing..")
        Solver.randomize(Cli._rc, moveCount)

    def display():
        print(Cli._rc)

        
if __name__ == "__main__":
    Cli.doCliThings()
