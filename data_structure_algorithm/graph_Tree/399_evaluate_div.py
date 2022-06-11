import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        def build_graph(equs,vals):
            def addEdge(s,d,val):
                if s in graph:
                    graph[s].append((d,val))
                else:
                    graph[s] = [(d,val)]
            for vertice,value in zip(equs,vals):
                s,d = vertice
                addEdge(s,d,value)
                addEdge(d,s,1/value)
        def find_path(query):
            s,d = query
            if s not in graph or d not in graph:
                return -1
            q = collections.deque([(s,1)])
            seen = set()
            while q:
                front, cur_prod = q.popleft()
                if front == d:
                    return cur_prod
                seen.add(front)
                for neighbor, val in graph[front]:
                    if neighbor not in seen:
                        q.append((neighbor,val*cur_prod))
            return -1
        build_graph(equations,values)
        return [find_path(q) for q in queries]

sol = Solution()

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(sol.calcEquation(equations, values, queries))