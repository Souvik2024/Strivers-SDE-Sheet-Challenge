class Stack:
    def __init__(self, capacity):
        self.arr = [0] * capacity
        self.size = capacity
        self.to = -1
    
    def push(self, num):
        if self.isFull():
            return
        self.to += 1
        self.arr[self.to] = num
    
    def pop(self):
        if self.isEmpty():
            return -1
        ans = self.arr[self.to]
        self.to -= 1
        return ans
    
    def top(self):
        if self.isEmpty():
            return -1
        return self.arr[self.to]
    
    def isEmpty(self):
        return self.to == -1
    
    def isFull(self):
        return self.to + 1 == self.size
