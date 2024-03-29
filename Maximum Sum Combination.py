import heapq
from heapq import heappop,  heappush,heapify
class Solution:
    def solve(self, A, B, C):
        A.sort(reverse=True)
        B.sort(reverse=True)
        n= len(A)
        pq= [(-(A[0]+B[0]),(0,0))]
        st=set()
        st.add((0,0))
        ans=[]
        while C>0:
            top= heappop(pq)
            ans.append(top[0]*-1)
            i= top[1][0]
            j= top[1][1]
            if i<n and j<n:
                if (i+1,j) not in st:
                    heappush(pq,(-(A[i+1]+B[j]),(i+1,j)))
                    st.add((i+1,j))
                if (i,j+1) not in st:
                    heappush(pq,(-(A[i]+B[j+1]),(i,j+1)))
                    st.add((i,j+1))
            C-=1
        return ans