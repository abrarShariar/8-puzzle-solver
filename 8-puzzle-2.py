class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(data):
        self.queue.append(data)
        if len(self.queue) > 1:
            # sort in ascending order
            isSorted = False
            while not isSorted:
                isSorted = True
                for i in range(len(self.queue) - 1):
                    if self.queue[i] > self.queue[i+1]:
                        isSorted = False
                        temp = self.queue[i]
                        self.queue[i] = self.queue[i+1]
                        selfgbhbnb .queue[i+1] = temp
    def display():
        print("Displaying Queue: ")
        for i in range(len(self.queue)):
            print(self.queue[i])


def main():
    priorityQueue = PriorityQueue()
    priorityQueue.enqueue(10)
    priorityQueue.enqueue(20)
    priorityQueue.enqueue(1)
    priorityQueue.enqueue(100)

    priorityQueue.display()

main()
