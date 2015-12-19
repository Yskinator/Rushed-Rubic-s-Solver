#!/usr/bin/env python3.5
from rubic import Cube as RubicCube
from solver import Solver

class Cli:
    def doCliThings():
        print("Hello! Welcome to Rushed Rubic's Cube!")
        print("Here's our cube!")
        rc = RubicCube()
        print(str(rc)+"\n\n")
        print("Let's randomize it!")
        print("How many random moves?")
        moveCount = int(input("Move count: "))
        print("Moving things!")
        Solver.randomize(rc, moveCount)
        print("The resulting cube!")
        print(rc)


if __name__ == "__main__":
    Cli.doCliThings()
