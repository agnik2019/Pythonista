class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n+1)]
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        color = [0 for _ in range(len(graph))]
        visited = [0 for _ in range(len(graph))]
        def dfs(u):
            for v in graph[u]:
                if visited[v] == False:
                    visited[v] = True
                    color[v] = not color[u]
                    if not dfs(v):
                        return False
                elif color[u] == color[v]:
                    return False
            return True
        for i in range(len(graph)):
            if visited[i] == False:
                if not dfs(i):
                    return False
        return True