# Constraints Based Sudoku Program
# Final project for AI class 
# Toby Baker and Thomas Denvir
# 4/30/2024
from numpy import array
from random import randint

unsolvedSudoku = "sudokuProblem.txt"
solvedSudoku = "sudokuSolution.txt"

def main():
    generateSudoku()


    return(0)

# Fills in initial values
def generateSudoku():
    
    puzzle = Puzzle()
    
    # Each index represents the number used
    # the value at each index is how many times it has been used
    # [0] represents empty boxes
    # For  simple or 'easy' sudoku, 3 of each number must be used and 3 numbers must be in each row, column, and box
    numCoords = [[[0, 0] for i in range(9)] for j in range(10)]
    numCts = [0 for i in range(10)]
    for layer in range(3):
        prevRow = [0, 0]
        prevCol = [0, 0]
        for numCt in range(3):
            if numCt != 0:
                while col != prevCol[numCt-1] and row != prevRow[numCt-1]:
                    col = randint(0,2)
                    row = randint(0,2)
            else:
                col = randint(0,2)
                row = randint(0,2)
            puzzle[numCt]





    puzzle.print(unsolvedSudoku)

# Solver
def solveSudoku(puzzle: list):
    solvedPuzzle = Puzzle()
    # Do some case based reasoning things here
    puzzle.print(solvedSudoku)


class Puzzle:
    # Initializes all values to 0
    def __init__(self):
        self.topLayer    = [Block() for i in range(3)]
        self.middleLayer = [Block() for i in range(3)]
        self.bottomLayer = [Block() for i in range(3)]
        self.solved = False

    # Overloads []
    def __getitem__(self, row: int, col: int):
        if row == 0:
            return self.topLayer[col]
        elif row == 1:
            return self.middleLayer[col]
        elif row == 2: 
            return self.bottomLayer[col]
        else:
            return ("No index at location " + str(row)+', '+str(col))
        
    # Prints out a puzzle to a given file
    def print(self):
        outputFile = unsolvedSudoku
        if self.solved:
            outputFile = solvedSudoku

        print("Printing to "+outputFile)
        with open(outputFile, 'w') as f:
            f.write(' -----------------------')
            for rowOfSquare in range(3):
                for innerRow in range(3):
                    f.write('\n')
                    for colOfSquare in range(3):
                        f.write('  ')
                        for innerCol in range(3):
                            f.write(str(self[rowOfSquare, innerRow][colOfSquare, innerCol])+' ')
                    
            f.write('\n -----------------------')

    

class Block:
    def __init__(self):
        self = [[0 for i in range(3)] for j in range(3)]
    
    def __getitem__(self, row: int, col: int):
        return self[row][col]
    def __setitem__(self, row: int, col: int, value: int):
        self[row][col] = value


if __name__ == "__main__":
    main()