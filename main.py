# Case Based Sudoku Program
# Final project for AI class 
# Toby Baker and Thomas Denvir
# 4/30/2024
from numpy import array

unsolvedSudoku = "sudokuProblem.txt"
solvedSudoku = "sudokuSolution.txt"

def main():
    generateSudoku()


    return(0)

# Fills in initial values
def generateSudoku():
    
    puzzle = blankPuzzle()
    
    # Each index represents the number used
    # the value at each index is how many times it has been used
    # [0] represents empty boxes
    # For  simple or 'easy' sudoku, 3 of each number must be used and 3 numbers must be in each row, column, and box
    usedNums = [0 for i in range(10)]

    printPuzzle(puzzle, unsolvedSudoku)

# Solver
def solveSudoku(puzzle: list):
    solvedPuzzle = blankPuzzle()
    # Do some case based reasoning things here
    printPuzzle(puzzle, solvedSudoku)

# Initializer
def blankPuzzle():
    # Initialize all the squares
    topLeftCorner = [[0 for i in range(3)] for j in range(3)]
    topRightCorner = topLeftCorner
    botLeftCorner = topLeftCorner
    botRightCorner = topLeftCorner
    center = topLeftCorner
    top = topLeftCorner
    bottom = topLeftCorner
    left = topLeftCorner
    right = topLeftCorner
    
    puzzle = [[topLeftCorner, top, topRightCorner],
                   [left, center, right],
                   [botLeftCorner, bottom, botRightCorner]]
    return puzzle

# Prints out a given puzzle to a given file
def printPuzzle(puzzle: list, outputFile: str):
    with open(outputFile, 'w') as f:
        f.write(' -----------------------')
        for rowOfSquare in range(3):
            for innerRow in range(3):
                f.write('\n')
                for colOfSquare in range(3):
                    f.write('  ')
                    for innerCol in range(3):
                        f.write(str(puzzle[rowOfSquare][innerRow][colOfSquare][innerCol])+' ')
                    
            f.write('\n -----------------------')



if __name__ == "__main__":
    main()