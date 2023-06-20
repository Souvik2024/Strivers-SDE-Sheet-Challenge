class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        count = 1
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                count += 1
                i += 1
        return count