class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.arr = [0] * 100001
        self.cnt = 0

    def enqueue(self, e):
        self.arr[self.rear % len(self.arr)] = e
        self.rear += 1
        self.cnt += 1

    def dequeue(self):
        if self.cnt == 0:
            return -1
        dequeuedElement = self.arr[self.front % len(self.arr)]
        self.arr[self.front % len(self.arr)] = -1
        self.front += 1
        self.cnt -= 1
        return dequeuedElement
