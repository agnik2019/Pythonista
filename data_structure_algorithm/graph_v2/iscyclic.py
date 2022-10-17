#User function Template for python3


class Solution:
    def dfs_check(self, node,adj,vis,pathvis):
        vis[node] = 1
        pathvis[node] = 1
        for u in adj[node]:
            if not vis[u]:
                if self.dfs_check(u,adj,vis,pathvis):
                    return True
            elif pathvis[u]:
                return True
        pathvis[node] = 0
        return False
        
        
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        vis = [0]*V
        pathvis = [0]*V
        
        for i in range(V):
            if not vis[i]:
                if self.dfs_check(i,adj,vis,pathvis):
                    return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends