import math
W,H = 3, 3

class Node:
    def __init__(self):
        self.board = [[]]
        self.blankX = 0
        self.blankY = 0
        self.manhattanD = 0
        self.level = 0
        self.cost = 0

class PriorityQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, node):
        self.queue.append(node)
        # sort queue ascending order
        isSorted = False
        while not isSorted:
            isSorted = True
            for i in range(len(self.queue)-1):
                if self.queue[i].cost > self.queue[i+1].cost:
                    isSorted = False
                    temp = self.queue[i]
                    self.queue[i] = self.queue[i+1]
                    self.queue[i+1] = temp

    def display(self):
        print("Displaying queue with cost: ")
        for i in range(len(self.queue)):
            print(self.queue[i].cost)

    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        if len(self.queue) <= 0:
            return True
        else:
            return False

def solvePuzzle(initialNode, goalBoard):
    level = 0
    pq = PriorityQueue()
    pq.enqueue(initialNode)

    while not pq.isEmpty():
        x = pq.dequeue()
        print("Level: ", x.level)
        print(x.board, "\n")
        if x.board == goalBoard:
            print("SOLVED AT: ", level)
            return
        else:
            # generate neighbours
            level = level + 1
            neighbourList = generateNeighbours(x.board)
            for i in range(len(neighbourList)):
                node = Node()
                node.board = neighbourList[i]
                # node.distance = calculateManhattanDistance(node.board, goalBoard)
                node.distance = calculateEuclideanDistance(node.board, goalBoard)
                node.level = level
                node.cost = node.distance + node.level 
                pq.enqueue(node)
                
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


def calculateManhattanDistance(testBoard, goalBoard):
    totalDistance = 0
    for i in range(len(testBoard)):
        for j in range(len(testBoard[i])):
            item = testBoard[i][j]
            x_current, y_current = i, j
            for m in range(len(goalBoard)):
                for n in range(len(goalBoard[m])):
                    if item == goalBoard[m][n] and item != 0:
                        x_goal = m
                        y_goal = n
                        # calculating manhattan distance
                        manhattan = abs(x_current - x_goal) + abs(y_current - y_goal)
                        totalDistance = totalDistance + manhattan

    return totalDistance;


def calculateEuclideanDistance(testBoard, goalBoard):
    totalDistance = 0
    for i in range(len(testBoard)):
        for j in range(len(testBoard[i])):
            x_current, y_current = i, j
            item = testBoard[i][j]
            for m in range(len(goalBoard)):
                for n in range(len(goalBoard[m])):
                    if item == goalBoard[m][n] and item != 0:
                        x_goal = m
                        y_goal = n
                        # calculating euclidiean distance
                        a = math.pow((x_current-x_goal), 2)
                        b = math.pow((y_current-y_goal), 2)
                        euclidean = math.sqrt(a+b)
                        totalDistance = totalDistance + euclidean

    return totalDistance
                    

def main():
    goal = [[1,2,3], [4,5,6], [7,8,0]]
    i1 = [[0,1,3], [4,2,5], [7,8,6]]
    initialNode = Node()
    initialNode.board = i1
    
    solvePuzzle(initialNode, goal)
   
     
main()
