def graphColoring(graph, k, V):
    
    #your code here
    def canAssign(i,j,graph,V):
        for k in range(V):
            if graph[i][k]==1 and color[k]==j:
                return False
        return True        
    def helper(graph,V,i):
        if i==V:
            return True
        for j in range(k):
            if canAssign(i,j,graph,V):
                color[i] = j
                if helper(graph,V,i+1):
                    return True
                color[i]=-1    
        return False
    color= [-1]*V
    return helper(graph,V,0)