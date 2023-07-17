class Solution:
    def isValid(self, s):
        if len(s)%2:
            return False
        stack=[]
        closing={')':'(','}':'{',']':'['}
        for c in s:
            if c not in closing:
                stack.append(c)
            else:
                if not stack or stack[-1]!=closing[c]:
                    return False
                stack.pop()
        return not stack