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

def generateSudoku(file=unsolvedSudoku):
    # Initialize all the squares
    topLeftCorner = array([[[0]*3]*3])
    topRightCorner = topLeftCorner
    botLeftCorner = topLeftCorner
    botRightCorner = topLeftCorner
    center = topLeftCorner
    top = topLeftCorner
    bottom = topLeftCorner
    left = topLeftCorner
    right = topLeftCorner
    
    #puzzle = array([[topLeftCorner, top, topRightCorner],
    #               [left, center, right],
    #               [botLeftCorner, bottom, botRightCorner]])
    puzzle = array([[[[0]*3]*3], [[[0]*3]*3], [[[0]*3]*3]]*3)

    print(puzzle)
    with open(file, 'w') as f:
        for rowOfSquare in range(3):
            for innerRow in range(3):
                for colOfSquare in range(3):
                    for innerCol in range(3):
                        f.write(str(puzzle[rowOfSquare][innerRow][colOfSquare][innerCol]))
                        if innerCol == 2:
                            f.write(' | ')
            f.write('------------------')

                    





if __name__ == "__main__":
    main()