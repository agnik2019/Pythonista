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
class Solution:
    def numProvinces(self, adj, V):
        # code here 
        edges = []
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1:
                    edges.append([i,j])
        res = V
        ds = DisjointSet(V)
        for n1,n2 in edges:
            res -= ds.union(n1,n2)
        return res
            
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends