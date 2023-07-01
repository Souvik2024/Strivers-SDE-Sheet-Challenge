class Solution:
    def maximumMeetings(self,n,start,end):
        v = []
        for i in range(n):
            a = start[i]
            b = end[i]
            v.append((b,a))
        v.sort()
        i = 0
        j = 1
        ans = 1
        while j < n:
            if v[i][0] < v[j][1]:
                ans += 1
                i = j
                j += 1
            else:
                j += 1
        return ans