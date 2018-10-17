W, H = 3, 3
# Node
class Node:
    def __init__(self):
        self.board = [[]]
        self.blankX = 0
        self.blankY = 0
        self.misplacedTiles = 0
        self.level = 0
        self.cost = 0
    
# priority queue
class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, node):
        self.queue.append(node)
        if len(self.queue) > 1:
            # sort in ascending order
            isSorted = False
            while not isSorted:
                isSorted = True
                for i in range(len(self.queue) - 1):
                    if self.queue[i].cost > self.queue[i+1].cost:
                        isSorted = False
                        temp = self.queue[i]
                        self.queue[i] = self.queue[i+1]
                        self.queue[i+1] = temp
    def dequeue(self):
        return self.queue.pop(0)
						
    def display(self):
        print("Displaying Queue: ")
        for i in range(len(self.queue)):
            print(self.queue[i].cost)
            
    def isEmpty(self):
        if len(self.queue) <= 0:
            return True
        else:
            return False

    def size(self):
        return len(self.queue)

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
                node.misplacedTiles = calculateMisplacedTiles(neighbourList[i], goalBoard)
                node.level = level
                node.cost = node.misplacedTiles + node.level 
                pq.enqueue(node)
                


def calculateMisplacedTiles(testBoard, goalBoard):
    count = 0
    for i in range(len(testBoard)):
        for j in range(len(testBoard[i])):
            if testBoard[i][j] !=0 and testBoard[i][j] != goalBoard[i][j]:
                count += 1

    return count
            

def main():
    n1 = Node()
    n1.cost = 10
    n2 = Node()
    n2.cost = 20
    n3 = Node()
    n3.cost = 1

    p1 = PriorityQueue()
    p1.enqueue(n2)
    p1.enqueue(n3)
    p1.enqueue(n1)

    #p1.display()
    i1 = [[1,2,3], [4,0,5], [6,7,8]]
    i2 = [[0,2,3], [6,5,4], [1,7,8]]
    i3 = [[2,8,3], [1,6,4], [7,0,5]]

    goal = [[1,2,3],[8,0,4],[7,6,5]]
    #print(generateNeighbours(i2))

    #print(calculateMisplacedTiles(i2, goal))
    initialNode = Node()
    initialNode.board = i3
    solvePuzzle(initialNode,goal)
    
main()
