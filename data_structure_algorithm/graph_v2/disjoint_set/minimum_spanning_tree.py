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
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        edges = []
        for i in range(V):
            for v,w in adj[i]:
                edges.append((i,v,w))
        edges.sort(key = lambda x : x[2])
        ds = DisjointSet(V)
        mstwt = 0
        for u,v,w in edges:
            if ds.find(u) != ds.find(v):
                mstwt += w
                ds.union(u,v)
        return mstwt
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends