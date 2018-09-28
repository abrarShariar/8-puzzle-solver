W,H = 3,3

# initial state (generate randomly)
initial = [
    [8,1,3],
    [4,0,2],
    [7,6,5]
]

# goal to reach
goal = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

# test nodes (for testing)
t1 = [
    [8,1,3],
    [4,0,2],
    [7,5,6]
]

t2 = [
    [1,8,3],
    [4,0,2],
    [7,6,5]
]

t3 = [
    [8,1,3],
    [4,0,2],
    [7,5,6]
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


# main script runs from here ----
def main():
    priorityQueue = PriorityQueue()
    n1 = Node(t1, 0, 3, t2)
    n2 = Node(t2, 0, 1, t3)
    n3 = Node(t3, 0, 2, t1)

    priorityQueue.enqueue(n1)
    priorityQueue.enqueue(n2)
    priorityQueue.enqueue(n3)

    while not priorityQueue.isEmpty():
        node = priorityQueue.dequeue()
        print(node.board)

main()
