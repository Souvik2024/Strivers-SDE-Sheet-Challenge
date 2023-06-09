class Solution:
    def majorityElement(self, nums):
        r=[]
        num=Counter(nums)
        for i in num.keys():
            if(num[i]>len(nums)/3):
                r.append(i)
        return r