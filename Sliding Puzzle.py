import sys
from heapq import heappush, heappop
import time


# class which representing a single game board
class GameBoard:
    def __init__(self, gameState):
        self.gameState = gameState

    # return the coordinate of certain value
    def findCord(self, value):
        goalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

        for i in range(3):
            for j in range(3):
                if goalState[i][j] == value:
                    return i, j

    # sum up all the man_dis of every single tile
    def calManthattan_dis(self):
        score = 0
        for i in range(3):
            for j in range(3):
                if self.gameState[i][j] == 0:
                    continue
                else:
                    score += self.calSingleTile(self.gameState[i][j], i, j)
        return score

    # cal the man_dis of a singel tile
    def calSingleTile(self, v, x, y):
        goalX, goalY = self.findCord(v)
        return abs(x - goalX) + abs(y - goalY)

    # return the coordinate of "0"
    def findZeroLoc(self):
        for i in range(3):
            for j in range(3):
                if(self.gameState[i][j] == 0):
                    return i, j

    # find all the valid(moveable neigbour)
    def findValidNe(self):
        validNeigbour = []
        x_axis = [1, 0, -1,  0]
        y_axis = [0, 1,  0, -1]

        zeroX, zeroY = self.findZeroLoc()
        for x, y in zip(x_axis, y_axis):
            newX = x+zeroX
            newY = y+zeroY
            if(self.checkLocValid(newX, newY) == True):
                newLoc = newX, newY
                validNeigbour.append(newLoc)
                newX = 0
                newY = 0
        return validNeigbour

    # check the coordinate is out of bound or not
    def checkLocValid(self, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
        else:
            return True

    def cloneBoard(self):
        board = []
        for row in self.gameState:
            board.append([x for x in row])
        return board

    # swap the place of "0" and incoming coordinate
    def makeMove(self, x, y):
        movedBoard = self.cloneBoard()
        orginalValue = movedBoard[x][y]

        zeroX, zeroY = self.findZeroLoc()
        movedBoard[x][y] = 0
        movedBoard[zeroX][zeroY] = orginalValue

        return movedBoard

    # get all the moved board which are valid
    def everyPossibleMove(self):
        neighbour = self.findValidNe()
        possibleBoards = []
        for i in neighbour:
            # print(self.makeMove(i[0], i[1]))
            possibleBoards.append(self.makeMove(i[0], i[1]))
        return possibleBoards

    # return the abc str value based on the coordinate
    def findOutput(self):
        output = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        letter = output[self.findZeroLoc()[0]
                        ][self.findZeroLoc()[1]]
        return letter


# the node class in noraml a* algo
class Node:

    def __init__(self, puzzle, parent=None):
        self.puzzle = puzzle
        self.parent = parent

        if (self.parent != None):
            self.costSoFar = parent.costSoFar + 1

        else:
            self.costSoFar = 0

    # obtain the hval which is = total manthattan dis of the board
    def heuristic(self):
        return self.puzzle.calManthattan_dis()

    # cal the fval = g+h
    def score(self):
        return (self.costSoFar + self.heuristic())

    def __lt__(self, otherNode):
        return self.score() < otherNode.score()

    # check whether is proceed to goal or not
    def checkEnd(self):
        goalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        return str(self.puzzle.gameState) == str(goalState)


def Astar(initState):

    # init open list
    openList = []
    closedList = []
    heappush(openList, initState)

    # iterate every element in openList
    while len(openList) > 0:

        # pop the smallest fval node in the openList
        first = heappop(openList)
        closedList.append(first)

        # check current element is the goal
        if first.checkEnd():
            return first

        # try every neighbour in of the current ele
        for move in first.puzzle.everyPossibleMove():
            # init the new node by using the neighbour move
            newGameBoard = GameBoard(move)
            newNode = Node(newGameBoard, first)

            # current move is already in the closed list
            if len([closed_child for closed_child in closedList if closed_child.puzzle.gameState == move]) > 0:
                continue

            # current move is already in the open list
            if len([open_node for open_node in openList if move == open_node.puzzle.gameState and newNode.costSoFar > open_node.costSoFar]) > 0:
                continue

            # push the current new Node into openlist and heapify the list
            heappush(openList, newNode)


input = sys.argv[1]

# obtain input into 3x3 list
initList = [[], [], []]
for i in range(9):
    if i < 3:
        initList[0].append(int(input[i]))
    elif i >= 3 and i < 6:
        initList[1].append(int(input[i]))
    else:
        initList[2].append(int(input[i]))

# init the board
initBoard = GameBoard(initList)
initNode = Node(initBoard)

# run astar
end = Astar(initNode)


# obtain the sequence
iterNode = end
sequence = []
while iterNode.parent != None:
    # prepend
    sequence.insert(0, iterNode.puzzle.findOutput())
    iterNode = iterNode.parent

# reverse the sequence
reverseStr = "".join(sequence)
print(reverseStr)
