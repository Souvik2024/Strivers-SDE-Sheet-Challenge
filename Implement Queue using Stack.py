class MyQueue(object):
    def __init__(self):
        self.queue = []
    def push(self, x):
        self.queue.insert(0, x)
    def pop(self):
        return self.queue.pop()
    def peek(self):
        return self.queue[-1]
    def empty(self):
        return self.queue == []