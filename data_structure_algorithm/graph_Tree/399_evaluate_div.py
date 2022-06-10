import collections
def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    G = collections.defaultdict(dict)
    for (x, y), v in zip(equations, values):
        G[x][y] = v
        G[y][x] = 1/v
    def bfs(src, dst):
        if not (src in G and dst in G): return -1.0
        q, seen = [(src, 1.0)], set()
        for x, v in q:
            if x == dst: 
                return v
            seen.add(x)
            for y in G[x]:
                if y not in seen: 
                    q.append((y, v*G[x][y]))
        return -1.0
    return [bfs(s, d) for s, d in queries]


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(calcEquation(equations, values, queries))