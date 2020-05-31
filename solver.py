from random import randint
from getSudoku import getSudoku

def printer(array):
    '''Prints fields in a 3x3 format'''
    for i in array:
        print(i)

def getSquares(field, pos):
    '''
    returns all numbers in the corresponding square for the number
    '''
    x = pos[0]
    y = pos[1]
    numsInSquare = []
    if x < 3:
        for i in range(3):
            for n in range(3):
                if field[i][y][n] != 0:
                    numsInSquare.append(field[i][y][n])
    elif x < 6:
        for i in range(3,6):
            for n in  range(3):
                if field[i][y][n] != 0:
                    numsInSquare.append(field[i][y][n])
    else:
        for i in range(6,9):
            for n in range(3):
                if field[i][y][n] != 0:
                    numsInSquare.append(field[i][y][n])
    return numsInSquare

def getHorizontal(field, pos):
    '''
    returns a list of numbers in the horizontal line for the number
    '''
    x = pos[0]
    numbers = []
    for i in field[x]:
        for nums in i:
            if nums != 0:
                numbers.append(nums)
    return numbers

def getVertical(field, pos):
    '''
    returns a list of numbers in the vertical line for the number 
    '''
    y = pos[1]
    z = pos[2]
    numbers = []
    for i in range(len(field)):
        if field[i][y][z] != 0:
            numbers.append(field[i][y][z])
    return numbers

def getEmptyPositions(field):
    '''
    Goes through all positions in the field
    returns positions of empty fields
    '''
    emptyPositions = []
    for line in range(len(field)):
        for third in range(len(field[line])):
            for place in range(len(field[line][third])):
                if field[line][third][place] == 0:
                    emptyPositions.append([line,third,place])
    return emptyPositions

def getAllowedNums(pos, field):
    '''Returns a list of numbers which are allowed in a position'''
    allowed = []
    for num in range(1,10):
        if num not in getHorizontal(field, pos) and num not in getVertical(field, pos) and num not in getSquares(field, pos):
            allowed.append(num)
    return allowed

def placeNum(field, pos, num):
    '''Places a number in the sudoku field'''
    x, y, z = pos[0], pos[1], pos[2]
    field[x][y][z] = num

def helper(field):
    '''
    Places numbers where only 1 number is possible
    '''
    emptyPositions = getEmptyPositions(field)
    numPlaced = False
    for position in emptyPositions:
        avialableNums = getAllowedNums(position, field)
        if len(avialableNums) == 1:
            placeNum(field, position, avialableNums[0])
            numPlaced = True
    if numPlaced:
        helper(field)

def sudokuSolver(field):
    '''
    Uses helper function to fill all the spaces with 1 avialable option.
    When only positions with multiple options are avialable places one of avialable numbers and tries to finish the solution
    If solution cannot be finished all changes that were made are reversed and the next possible number for the position is entered
    '''
    helper(field)
    emptyPositions = getEmptyPositions(field)
    if len(emptyPositions) != 0:
        for position in emptyPositions:
            allowedNums = getAllowedNums(position, field)
            for num in allowedNums:
                placeNum(field, position, num)
                sudokuSolver(field)
                placeNum(field, position, 0)
    helper(field)

def showTheAnswer():
    filledSudoku = getSudoku()
    print()
    print("Unsolved sudoku")
    printer(filledSudoku)
    print("---------------------------------")
    print("Solution:")
    sudokuSolver(filledSudoku)
    printer(filledSudoku)

showTheAnswer()