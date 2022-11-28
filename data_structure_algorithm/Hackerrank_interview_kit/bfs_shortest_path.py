from collections import defaultdict
from collections import deque

def bfs(n, m, edges, s):
    graph = defaultdict(list)
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)
        
    dists = defaultdict(lambda: -1)
    dists[s] = 0
    queue = deque([s])
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if dists[neighbor] < 0:
                queue.append(neighbor)
                dists[neighbor] = dists[v] + 6
    return [dists[i] for i in range(1, n+1) if i != s]
    
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    edges = []
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        edges.append([x,y]) 
    s = int(input())
    res = bfs(n, m, edges, s)
    for r in res:
        print(r,end=" ")
    print()
