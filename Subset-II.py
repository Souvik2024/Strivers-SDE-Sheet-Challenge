class Solution:
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        res = []
        self.backtrack(0, [], res, nums)
        return res
    def backtrack(self, index, curr, res, nums):
        res.append(curr[:])
        for i in range(index, len(nums)):
            if (i>index and nums[i-1] == nums[i]):
                continue
            curr.append(nums[i])
            self.backtrack(i+1, curr, res, nums)
            curr.pop()