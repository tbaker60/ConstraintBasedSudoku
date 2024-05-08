# Constraints Based Sudoku Program
# Final project for AI class 
# Toby Baker and Thomas Denvir
# 4/30/2024
from random import seed, randint, choice
from pandas import Series

unsolvedSudoku = "sudokuProblem.txt"
solvedSudoku = "sudokuSolution.txt"

def main():
    puzzle = Puzzle()
    if input("Generate easy puzzle [y]? ") == 'y':
        puzzle.createEasy()
    if input("Solve [y]?"):
        puzzle.solve()

    return(0)

"""# Fills in initial values
def generateSudoku():
    seedNum = randint(1,10)
    seed(seedNum)
    puzzle = Puzzle()
    
    # Each index represents the number used
    # the value at each index is how many times it has been used
    # [0] represents empty boxes
    # For  simple or 'easy' sudoku, 3 of each number must be used and 3 numbers must be in each row, column, and box
    #numCoords = [0 for j in range(10)]

    numCts = [0 for i in range(10)]

    for num in range(10):
        if num != 0:
            firstRows = [-1, -1]
            firstCols = [-1, -1]
            prevRows = [-1, -1]
            prevCols = [-1, -1]
            i = 3
            for j in range(i):
                rows = [randint(0,2), randint(0,2)]
                cols = [randint(0,2), randint(0,2)]
                # while in same block or same row or same column 
                checkPrev = (rows[0] == prevRows[0] and cols[0] == prevCols[0]) or (rows == prevRows) or (cols == prevCols)
                checkFirst = (rows[0] == firstRows[0] and cols[0] == firstCols[0]) or (rows == firstRows) or (cols == firstCols)
                collisionCt = 0
                while checkFirst or checkPrev or puzzle[rows[0]][cols[0]][rows[1]][cols[1]] != 0:
                    #print("Collision at: " + str(rows[0]) + ' ' + str(cols[0]) + ' ' + str(rows[1])+ ' ' + str(cols[1]))
                    #print("         and: " + str(prevRows[0]) + ' ' + str(prevCols[0]) + ' ' + str(prevRows[1])+ ' ' + str(prevCols[1]))
                    #print("  for number: " + str(num))
                    #print("Evals: " + str(rows[0] == prevRows[0] and cols[0] == prevCols[0]) + " " + str(rows == prevRows) + ' ' + str(cols == prevCols))
                    #print("       " + str(((rows[0] == prevRows[0] and cols[0] == prevCols[0]) or (rows == prevRows) or (cols == prevCols))))
                    #print("collision on first: " + str(checkFirst) + " prev: "+str(checkPrev)+ " with " + str(num) + " and ct " + str(collisionCt))

                    rows = [randint(0,2), randint(0,2)]
                    cols = [randint(0,2), randint(0,2)]
                    collisionCt += 1

                    if collisionCt >= 3:
                        if firstCols[0] != -1:
                            puzzle[firstRows[0]][firstCols[0]][firstRows[1]][firstCols[1]] = 0
                        if prevRows[0] != -1:
                            puzzle[prevRows[0]][prevCols[0]][prevCols[1]][prevRows[1]] = 0
                        prevCols = [-1, -1]
                        prevRows = [-1, -1]
                    #if collisionCt > 15:
                        #break

                firstCols = prevCols
                firstRows = prevRows
                prevCols = cols
                prevRows = rows
                numCts[num] += 1
                puzzle[rows[0]][cols[0]][rows[1]][cols[1]] = num
    puzzle.createEasy()
    puzzle.print()
"""

class Puzzle:
    # Initializes all values to 0
    def __init__(self):
        self.topLayer    = [Block(0, i) for i in range(3)]
        self.middleLayer = [Block(1, i) for i in range(3)]
        self.bottomLayer = [Block(2, i) for i in range(3)]
        self.solved = True
        self.print()
        self.solved = False
        self.print()

    # Overloads #[]
    def __getitem__(self, row: int):
        if row == 0:
            return self.topLayer
        elif row == 1:
            return self.middleLayer
        elif row == 2: 
            return self.bottomLayer
        else:
           return ("No index at location " + str(row))
        

    def createEasy(self):
        nums = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9]
        aNum = choice(nums)

        for i in range(9):
            if i == 0:
                #1
                self[0][1][2][2] = aNum
                self[1][1][2][1] = aNum
                self[2][0][0][1] = aNum
                self[2][1][1][0] = aNum
                self[2][2][2][0] = aNum
            elif i == 1:
                #2
                self[0][1][2][1] = aNum
                self[1][2][2][1] = aNum
                self[2][1][1][2] = aNum
                self[2][2][0][0] = aNum
                              
            elif i == 2:
                #3
                self[0][0][2][2] = aNum
                self[0][1][1][1] = aNum
                self[1][0][0][1] = aNum
                self[1][2][1][1] = aNum
                self[2][0][0][0] = aNum
                self[2][2][1][2] = aNum
            elif i == 3:
                #4
                self[0][0][0][2] = aNum
                self[0][1][1][2] = aNum
                self[0][2][2][1] = aNum
                self[1][2][0][0] = aNum
            elif i == 4:
                #5
                self[0][1][0][1] = aNum
                self[1][0][0][2] = aNum
            elif i == 5:
                #6
                self[0][2][1][0] = aNum
                self[1][0][2][2] = aNum
                self[2][1][2][1] = aNum
            elif i == 6:
                #7
                self[0][1][1][0] = aNum
                self[1][0][2][1] = aNum
                self[2][1][0][1] = aNum
            elif i == 7:
                #8
                self[1][2][0][1] = aNum
                self[2][1][1][1] = aNum
            elif i == 8:
                #9
                self[0][0][1][0] = aNum
                self[0][2][2][2] = aNum
                self[1][1][0][1] = aNum
                self[1][0][1][1] = aNum
                self[1][2][2][0] = aNum
                self[2][0][1][2] = aNum
                self[2][1][0][0] = aNum
            if i != 8 :
                nums.remove(aNum)
                aNum = choice(nums)
        self.print()



    def solve(self):
        nums = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9]
        numCts = [0 for i in range(9)]
        rowContains = [[False for i in range(9)] for j in range(9)]
        colContains = [[False for i in range(9)] for j in range(9)]
        blockContains = [[False for i in range(9)] for j in range(9)]
        for u in range(9):
            for i in range(3):
                for j in range(3):
                    coords = self[i][j].find(nums[u])
                    if coords != [-1, -1]:
                        numCts[u] += 1
                        if i == 0:
                            rowContains[coords[0]][u] = True
                            blockContains[j][u] = True
                        if j == 0:
                            colContains[coords[1]][u] = True
                        if i == 1:
                            rowContains[coords[0]+3][u] = True
                            blockContains[j+3][u] = True
                        if j == 1:
                            colContains[coords[1]+3][u] = True
                        if i == 2:
                            rowContains[coords[0]+6][u] = True
                            blockContains[j+6][u] = True
                        if j == 2:
                            colContains[coords[1]+6][u] = True
        
        for num in range(9):
            if numCts[num] < 9:
                for block in range(9):
                    if blockContains[block][num] == False:
                        i = 0
                        colCheck = [True, int]
                        rowCheck = [True, int]
                        if block < 3:
                            for i in range(3):
                                rowCheck = [rowContains[i][num], i]
                                if rowCheck[0]:
                                    break
                        elif block < 6:
                            i = 3
                            for i in range(6):
                                rowCheck = [rowContains[i][num], i]
                                if rowCheck[0]:
                                    break
                        else:
                            i = 6
                            for i in range(9):
                                rowCheck = [rowContains[i][num], i]
                                if rowCheck[0]:
                                    break
                        
                        if block in [0, 3, 6]:
                            for i in range(3):
                                if colContains[i][num] == False:
                                    colCheck = [False, i]
                        elif block in [1, 4, 7]:
                            i = 3
                            for i in range(6):
                                if colContains[i][num] == False:
                                    colCheck = [False, i]
                        else: 
                            i = 6
                            for i in range(9):
                                if colContains[i][num] == False:
                                    colCheck = [False, i]

                        
                        if colCheck[0]== False and rowCheck[0]== False:
                            col = 0
                            blockCol = 0
                            row = 0
                            blockRow = 0
                            if colCheck[1] < 3:
                                col = colCheck[1]
                            elif colCheck[1] < 6:
                                col = colCheck[1]-3
                                blockCol = 1
                            else:
                                col = colCheck[1]-6
                                blockCol = 2
                                

                            if block < 3:
                                row = rowCheck[1]
                                blockRow = 0
                            elif block < 6:
                                row = rowCheck[1] - 3
                                blockRow = 1
                            else:
                                row = rowCheck[1]-6
                                blockRow = 2
                            
                            self[blockRow][blockCol][row][col] = num

        self.solved = True
        self.print()

    # Prints out a puzzle to a given file
    def print(self):
        outputFile = unsolvedSudoku
        if self.solved:
            outputFile = solvedSudoku

        print("Printing to "+outputFile)
        with open(outputFile, 'w') as f:
            f.write(' -----------------------')
            for layer in range(3):
                for blockCol in range(3):
                    f.write('\n')
                    for row in range(3):
                        f.write('  ')
                        for col in range(3):
                            #print(str(layer) + ' ' + str(blockCol) + ' '+ str(row) + ' ' + str(col))
                            f.write(str(self[layer][row][blockCol][col])+' ')
                    
                f.write('\n -----------------------')
            f.close()

    

class Block:
    def __init__(self, layer, col):
        #self.cells = [['a', 'b', 'c'] for j in range(3)]
        self.cells = [[0 for i in range(3)] for j in range(3)]
        self.coords = [layer, col]
    
    def __getitem__(self, row: int):
        return self.cells[row]

    def find(self, num: int):
        for i in range(3):
            if num in self.cells[i]:
                return [i, self.cells[i].index(num)]
        return [-1, -1]


if __name__ == "__main__":
    main()