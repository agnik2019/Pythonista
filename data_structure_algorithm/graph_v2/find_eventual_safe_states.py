class Solution:
    def dfs_check(self, node,adj,vis,pathvis,checknode):
        vis[node] = 1
        pathvis[node] = 1
        checknode[node] = 0
        for u in adj[node]:
            if not vis[u]:
                if self.dfs_check(u,adj,vis,pathvis,checknode):
                    checknode[node] = 0
                    return True
            elif pathvis[u]:
                checknode[node] = 0
                return True
        checknode[node] = 1 # cycle not found
        pathvis[node] = 0
        return False
    def eventualSafeNodes(self, adj: List[List[int]]) -> List[int]:
        V = len(adj)
        safenodes = []
        vis = [0]*V
        pathvis = [0]*V
        checknode = [0]*V
        
        for i in range(V):
            if not vis[i]:
                self.dfs_check(i,adj,vis,pathvis,checknode)
        #return False
        for i in range(V):
            if checknode[i]:
                safenodes.append(i)
        return safenodes