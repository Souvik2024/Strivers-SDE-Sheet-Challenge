def isPossible(stalls,k,mid):
    cowcount=1
    lastpos=stalls[0]
    for i in range(len(stalls)):
        if(stalls[i]-lastpos>=mid):
            cowcount+=1
            if(cowcount==k):
                return True
            lastpos=stalls[i]
    return False           
def aggressiveCows(stalls, k):
    stalls=sorted(stalls)
    s=0
    e=max(stalls)
    ans=-1
    while(s<=e):
        mid=s+(e-s)//2
        if(isPossible(stalls,k,mid)):
            ans=mid
            s=mid+1
        else:
            e=mid-1
    return(ans)