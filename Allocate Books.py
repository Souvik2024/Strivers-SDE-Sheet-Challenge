class Solution:
	def books(self, A, B):
        def allocationISpossible(m):
            allocated,pages=1,0
            for i in range(len(A)):
                if A[i]>m: return False
                if pages+A[i]>m:
                    allocated+=1
                    pages=A[i]
                else: pages+=A[i]
            if allocated>B: return False
            return True
        res=-1
        if B>len(A): return -1
        l=A[0]
        r=sum(A)
        while l<=r:
            mid=(l+r)//2
            if allocationISpossible(mid):
                res=mid
                r=mid-1
            else: l=mid+1
        return l