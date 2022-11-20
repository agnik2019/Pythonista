'''
This is a leetcode premium problem

Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

'''
class DisjointSet:
    def __init__(self,n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [1]*n

    def find(self,u):
        if u == self.par[u]:
            return u
        self.par[u] = self.find(self.par[u])
        return self.par[u]
    
    def union(self,n1,n2):
        p1,p2  = self.find(n1),self.find(n2)
        if p1 == p2: return 0
        if self.rank[p1]< self.rank[p2]:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        return 1
        
def connected_componets(n,edges):
    # n -> nodes
    ds = DisjointSet(n)
    res = n
    for n1,n2 in edges:
        res -= ds.union(n1,n2)
    return res


# Driver code
n = 7
edges = [[0,1],[1,2],[3,4],[5,6],[4,5]]

print(connected_componets(n,edges))