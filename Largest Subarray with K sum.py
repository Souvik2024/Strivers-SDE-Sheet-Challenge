class Solution:
    def maxLen(self, n, arr):
        #Code here
        arr = [0] + arr
        n += 1
        sum_arr = [0 for i in range(n)]
        sum_arr[0] = arr[0]
        key_ent = dict()
        key_ent[arr[0]] = 0
        for i in range(1, n):
            sum_arr[i] = sum_arr[i-1] + arr[i]
            if sum_arr[i] not in key_ent:
                key_ent[sum_arr[i]] = i
        res_len = 0
        for i in range(n):
            res_len = max(res_len, i - key_ent[sum_arr[i]])
        return res_len