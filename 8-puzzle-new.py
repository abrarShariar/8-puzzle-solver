from __future__ import print_function
W, H = 3, 3

# node
class Node:
    def __init__(self):
        self.parent = [[]]
        self.mat = [[]]
        self.x = 0
        self.y = 0
        self.cost = 0
        self.level = 0


# print matrix
def printMatrix(mat):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print("\n")


# to make a new node
def newNode(mat, x, y, newX, newY, level, parent):
    node = Node()
    node.parent = parent
    node.mat = mat
    # move title by 1 pos
    tmp = node.mat[x][y]
    node.mat[x][y] = node.mat[newX][newY]
    node.mat[newX][newY] = tmp

    node.cost = sys.maxint
    node.level = level
    node[x] = newX
    node[y] = newY

    return node

def findBlank(board):
    x, y = 0, 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                x, y = i, j
                break
    return x, y

def solveBoard(initial, x, y, goal):


def main():
    # initial board
    initial = [
        [1, 2, 3],
        [5, 6, 0],
        [7, 8, 4]
    ]

    # goal board
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    # blank positions of initial board
    x, y = findBlank(initial)
    solveBoard(initial, x, y, goal)


main()
