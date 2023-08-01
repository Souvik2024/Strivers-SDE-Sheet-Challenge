from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        ans = [0] * (n - k + 1)
        dq = deque()
        ri = 0
        for i in range(n):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                ans[ri] = nums[dq[0]]
                ri += 1
        return ans 