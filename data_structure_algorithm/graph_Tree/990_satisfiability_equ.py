class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = defaultdict(set)
        def addEdge(u,v):
            graph[u].add(v)
            graph[v].add(u)
        def dfs(u,target,visited):
            if u == target:
                return True
            visited.add(u)
            for edge in graph[u]:
                if edge in visited:
                    continue
                if dfs(edge, target, visited):
                    return True
            return False
        notequals = []
        for equ in equations:
            if equ[1:3] == "!=":
                notequals.append([equ[0],equ[3]])
            else:
                addEdge(equ[0],equ[3])
        for u,v in notequals:
            if dfs(u,v,set()):
                return False
        return True
        