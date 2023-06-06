class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x: x[0])
        result = []
        for start, end in intervals:
            if not result or result[-1][1] < start:
                result.append([start, end])
            else:
                result[-1] = [result[-1][0], max(end, result[-1][1])]
        return result