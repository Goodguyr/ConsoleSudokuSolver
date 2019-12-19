from random import randint
from getSudoku import sudokuInfo

def makeField():
    '''
    Creates and returns an array containing 9 arrays
    containing 3 arrays each
    containing 3 placeholders for 0
    One line --> [[0,0,0],[0,0,0],[0,0,0]]
    '''
    field =[]
    for numOfLines in range(9):
        line = []
        field.append(line)
        for numOfSquares in range(3):
            square = []
            line.append(square)
            for spaceHolders in range(3):
                square.append(0)
    return field

sudoku = makeField()

def printer(array):
    '''Prints fields in a 3x3 format'''
    for i in array:
        print(i)


#x y z coordinates for position 
#x - chooses in which line the num is, x ranges from 0 to 8
#y - chooses in which box the number is, y ranges from 0 to 2
#z - chooses in which position the number is, z ranges from 0 to 2
#coordinate will be sent as [x,y,z]


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
                numsInSquare.append(field[i][y][n])
    elif x < 6:
        for i in range(3,6):
            for n in  range(3):
                numsInSquare.append(field[i][y][n])
    else:
        for i in range(6,9):
            for n in range(3):
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
        numbers.append(field[i][y][z])
    return numbers


def checkForSame(nums):
    '''
    Checks if array of numbers has duplicate elements
    returns False if no duplicates
   returns True if duplictes are found 
    '''
    newList = []
    for i in nums:
        if i != 0:
            newList.append(i)
    if len(newList) == len(set(newList)):
        return False
    return True


"""
get possible values from square
get possible values from horizontal
get possible values from vertical

pick option with smallest amount of options
"""

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


#def leastOptions(emptyPos, field):

def getRandPosition():
    x, y, z = randint(0,8), randint(0,2), randint(0,2)
    return [x,y,z]

def checkIfEmpty(pos):
    '''
    Checks if position already contains a number
    if not offers a new empty position
    returns empty position
    '''
    x = pos[0]
    y = pos[1]
    z = pos[2]
    if sudoku[x][y][z] != 0:
        nextPos = getRandPosition()
        return checkIfEmpty(nextPos)
    return pos

def checkIfAllowed(num, h, v, sq):
    '''
    checks if a number is allowed 
    if not returns an allowed number
    '''
    if not(num in h) and not(num in v) and not(num in sq):
        return num
    nextNum = randint(1,9)
    return checkIfAllowed(nextNum, h, v, sq)


def generateSudoku(field):
    '''
    function will generate 30 random clues
    minimum amount of clues for a sudoku to be solvable is 17
    30 clues is considered as a hard difficulty sudoku

    '''
    numOfClues = 30

    for i in range(numOfClues):
        randPos = getRandPosition()
        randPos = checkIfEmpty(randPos)
        hrz = getHorizontal(field, randPos)
        vrt = getVertical(field, randPos)
        sqr = getSquares(field, randPos)
        placeNum = randint(1,9)
        placeNum = checkIfAllowed(placeNum, hrz, vrt, sqr)
        x, y, z = randPos[0], randPos[1], randPos[2]
        sudoku[x][y][z] = placeNum

#def solveMySudoku(field):


generateSudoku(sudoku)


printer(sudoku)
