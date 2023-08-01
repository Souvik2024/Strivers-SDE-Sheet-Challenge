class Solution:
    def prevSmaller(self, A):
        st = []
        n = len(A)
        g = [0] * n
        for i in range(n):
            while st and st[-1] >= A[i]:
                st.pop()
            if i < n:
                if st:
                    g[i] = st[-1]
                else:
                    g[i] = -1
            st.append(A[i])
        return g