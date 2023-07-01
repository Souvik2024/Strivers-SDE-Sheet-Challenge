class Solution:    
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        platforms = 1
        result = 1
        i=1
        j=0
        while(i < n and j < n):
            if(arr[i] <= dep[j]):
                platforms = platforms + 1
                i = i + 1
            elif(arr[i] > dep[j]):
                platforms = platforms - 1
                j = j + 1
            if(platforms >  result):
                result = platforms
        return result