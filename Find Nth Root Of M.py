def findNthRootOfM(n,m):
   eps = 1e-8
   low = 1
   high = m
   mid = 0.0
   while (high-low)>eps:
       mid = (low+high)/2.0
       if mul(n,mid)<m:          
           low = mid
       else:
           high=mid
   return ("%.6f" %low)