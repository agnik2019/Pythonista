#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
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
    def get_parent(self):
        return self.par
        
class Solution:
    def Solve(self, n, adj):
        # Code here
        ds = DisjointSet(n)
        extra = 0
        for u,v in adj:
            if ds.find(u) == ds.find(v):
                extra += 1
            else:
                ds.union(u,v)
        comp = 0
        parent = ds.get_parent()
        for i in range(len(parent)):
            if parent[i] == i: comp += 1
        if extra >= comp -1: return comp-1
        return -1
            

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        adj = [list(map(int, input().split())) for _ in range(m)]
        ob = Solution()
        res = ob.Solve(n, adj)
        print(res)
# } Driver Code Ends