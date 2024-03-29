class Solution:
    def myAtoi(self, s):
        i = res = 0
        op = 1
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] in '+-':
            op = 1 if s[i] == '+' else -1
            i += 1
        MAX_RES = (1 << 31) - 1 if op == 1 else 1 << 31
        while i < len(s) and s[i].isdigit() and res <= MAX_RES:
            res = res * 10 + int(s[i])
            i += 1
        return min(res, MAX_RES) * op