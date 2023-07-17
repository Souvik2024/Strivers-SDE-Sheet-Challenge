class MedianFinder:
    def __init__(self):
        self.ref_array = []
        self.length = 0
    def addNum(self, num):
        low = 0
        high = self.length - 1
        while low <= high:
            mid = (low+high)//2
            if self.ref_array[mid] >= num:
                high = mid - 1
            else:
                low = mid + 1
        self.ref_array.insert(low,num)
        self.length += 1
    def findMedian(self):
        if self.length % 2 == 0:
            temp = self.length // 2
            return (self.ref_array[temp]+self.ref_array[temp-1])/2.0
        else:
            return self.ref_array[self.length // 2]