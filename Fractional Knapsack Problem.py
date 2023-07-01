class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
class Solution:    
    def fractionalknapsack(self, W,arr,n):
        li=[]
        for i in range(n):
            perUnitVal = arr[i].value/arr[i].weight
            li.append((perUnitVal,arr[i]))
        li.sort(key = lambda x:x[0], reverse=True)
        profit=0
        for pair in li:
            if pair[1].weight<=W:
                profit+=pair[1].value
                W-=pair[1].weight
            else:
                profit+=pair[0]*W
                W=0
                break
        return profit