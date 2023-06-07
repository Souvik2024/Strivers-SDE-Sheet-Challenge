class Solution:
    def findDuplicate(self, nums):
        l = len(nums)
        c = Counter(nums)
        for i in c:
            if(c[i] >= 2):
                return i