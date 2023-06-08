class Solution:
    def repeatedNumber(self, A):
        n = len(A)
        x = 0
        y = 0
        for i in range(n):
            e = (i+1)
            x += (A[i] - e)
            y += ((A[i] - e)*(A[i]+e))
        z = y//x
        r = (x+z)//2
        m = abs(z-r)
        v = []
        v.append(r)
        v.append(m)
        return v