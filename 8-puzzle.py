from __future__ import print_function

W,H = 3,3

# initial state (generate randomly)
initial = [
    [1,2,3],
    [5,6,0],
    [7,8,4]
]

# goal to reach
goal = [
    [1,2,3],
    [5,8,6],
    [0,7,4]
]

# test nodes (for testing)
t1 = [
    [0,1,3],
    [4,8,2],
    [7,5,6]
]

t2 = [
    [1,0,3],
    [4,8,2],
    [7,6,5]
]

t3 = [
    [8,1,0],
    [4,3,2],
    [7,5,6]
]

t4 = [
    [8,1,2],
    [4,3,0],
    [7,5,6]
]

t5 = [
    [8,1,2],
    [0,3,4],
    [7,5,6]
]

t6 = [
    [8,1,2],
    [7,3,4],
    [0,5,6]
]

t7 = [
    [8,1,2],
    [7,3,4],
    [5,0,6]
]

t8 = [
    [8,1,2],
    [7,3,4],
    [5,6,0]
]


class Node:
    def __init__(self, board=[[0 for x in range(W)] for y in range(H)], moves=0, priority=0, prev=None):
        self.board = board
        self.moves = moves
        self.priority = priority
        self.prev = prev

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i].priority < self.queue[min].priority:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()

# function to generate neighbouring nodes
def generateNeighbours(board):
    #locate the blank
    x, y = 0, 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                x, y = i, j
                break

    #generate neighbouring nodes
    neighbourList = []
    # horizontal right
    x1, y1 = x, y
    while y1 <= H-1:
        y1 += 1
        if y1 <= H-1:
            element = board[x1][y1]
            newBoard = list(map(list, board))
            newBoard[x1][y1] = 0
            newBoard[x][y] = element
            # print("FROM HORI-RIGHT")
            # print(newBoard)
            neighbourList.append(newBoard)
            break
        else:
            break

    # horizontal left
    x1, y1 = x, y
    while y1 >= 0:
        y1 -= 1
        if y1 >= 0:
            element = board[x1][y1]
            newBoard = list(map(list, board))
            newBoard[x1][y1] = 0
            newBoard[x][y] = element
            # print("FROM HORI-LEFT")
            # print(newBoard)
            neighbourList.append(newBoard)
            break
        else:
            break

    # vertically up
    x1, y1 = x, y
    while x1 <= W-1:
        x1 += 1
        if x1 <= W-1:
            element = board[x1][y1]
            newBoard = list(map(list, board))
            newBoard[x1][y1] = 0
            newBoard[x][y] = element
            # print("FROM VER-UP")
            # print(newBoard)
            neighbourList.append(newBoard)
            break
        else:
            break

    # vertically down
    x1, y1 = x, y
    while x1 >= 0:
        x1 -= 1
        if x1 >= 0:
            element = board[x1][y1]
            newBoard = list(map(list, board))
            newBoard[x1][y1] = 0
            newBoard[x][y] = element
            # print("FROM VER-DOWN")
            # print(newBoard)
            neighbourList.append(newBoard)
            break
        else:
            break

    return neighbourList

#Manhattan priority function
def calculatePriority(board, moves=0):
    #pick each element and calculate distance
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    totalDiff = 0
    # loop over test board
    for i1 in range(len(board)):
        for j1 in range(len(board[i1])):
            if board[i1][j1] != 0:
                # loop over goal board to find the item's pos
                for i2 in range(len(goal)):
                    for j2 in range(len(goal[i2])):
                        if goal[i2][j2] == board[i1][j1]:
                            totalDiff += abs(i1-i2) + abs(j1-j2)

    return totalDiff + moves

# compare with goal node
def compare(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != goal[i][j]:
                return False
    return True


def printMatrix(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print("\n")


def main():

    currentBoard = initial
    moves = 0
    print(compare(currentBoard))

    while compare(currentBoard) == False:
        print("Move: ", moves)
        print("current board: ")
        printMatrix(currentBoard)

        childList = generateNeighbours(currentBoard)
        moves += 1

        print("Child List:")
        for i in range(len(childList)):
            print("Child index: ", i)
            printMatrix(childList[i])

        min = calculatePriority(childList[0], moves)
        minIndex = 0
        for i in range(len(childList)):
            priority = calculatePriority(childList[i], moves)
            if priority < min:
                min = priority
                minIndex = i

        currentBoard = childList[minIndex]

    print("final board")
    printMatrix(currentBoard)


main()
