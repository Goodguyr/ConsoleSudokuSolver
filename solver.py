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

def checkForSame(nums):
    '''
    Checks if array of numbers has duplicate elements
    returns False if no duplicates
   returns True if duplictes are found 
    '''
    newList = nums
    if len(newList) == len(set(newList)):
        return False
    return True

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

def leastOptions(emptyPos, field):
    '''
    Finds which empty positions have smallest amount of possible answers
    returns an array with position of the field with smallest amount of possible answers
    '''
    bestSqrs = []
    for onePos in emptyPos:
        if 9 - len(getHorizontal(field, onePos)) <= 4:
            bestSqrs.append(onePos)
        elif 9 - len(getVertical(field, onePos)) <= 4:
            bestSqrs.append(onePos)
    return bestSqrs

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

def sudokuSolver(field):
    '''
    Places numbers where only 1 number is possible
    When no places with one possible option exists checks the field till its solved
    '''
    emptyPositions = getEmptyPositions(field)
    least = leastOptions(emptyPositions, field)
    counter = 0
    for position in least:
        allowedNums = getAllowedNums(position, field)
        if len(allowedNums) == 1:
            placeNum(field, position, allowedNums[0])
        else:
            counter = counter + 1
    if counter == len(least) and counter != 0:
        position = least[0]
        allowedNums = getAllowedNums(position, field)
        placeNum(field, position, allowedNums[0])
    if len(emptyPositions) != 0:
        return sudokuSolver(field)

print()
print("Unsolved sudoku")
filledSudoku = getSudoku()
printer(filledSudoku)
print("---------------------------------")
print("Solution:")
sudokuSolver(filledSudoku)
printer(filledSudoku)