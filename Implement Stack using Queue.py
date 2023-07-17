class MyStack:
    def __init__(self):
        self.queue = []
    def push(self, x):
        size = len(self.queue)
        self.queue.append(x)
        for _ in range(size):
            val = self.queue.pop(0)
            self.queue.append(val)
    def pop(self):
        return self.queue.pop(0)
    def top(self):
        return self.queue[0]
    def empty(self):
        return True if len(self.queue)==0 else False