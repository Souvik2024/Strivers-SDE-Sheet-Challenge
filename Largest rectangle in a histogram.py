class Solution:
    def largestRectangleArea(self, heights):
        n=len(heights)
        st=[(heights[-1],n-1)]
        left=[1]*n
        right=[1]*n
        for i in range(n-2,-1,-1):
            while st and st[-1][0]>=heights[i]:
                st.pop()
            if len(st)==0:
                left[i]=n-i
            elif st[-1][0]<heights[i]:
                left[i]=st[-1][1]-i
            st.append((heights[i],i))
        st=[]
        maxArea=0
        for i in range(n):
            while st and st[-1][0]>=heights[i]:
                st.pop()
            if len(st)==0:
                right[i]=i+1
            elif st[-1][0]<heights[i]:
                right[i]=i-st[-1][1]
            st.append((heights[i],i))
            maxArea=max(maxArea,(left[i]+right[i]-1)*heights[i])
        return maxArea