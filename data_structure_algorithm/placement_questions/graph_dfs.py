from collections import defaultdict


def main(paths,start):
    adjlist = defaultdict(list)
    for p in paths:
        adjlist[p[0]].append(p[1])

    visited = set()
    res = []

    def dfs(start):
        res.append(start)
        if start not in visited:
            visited.add(start)
        adjacent_nodes = adjlist[start]
        for node in adjacent_nodes:
            dfs(node)
    dfs(start)
    return res


paths=[["Bangalore","Hyderabad"],
        ["Bangalore","Chennai"],
        ["Hyderabad","Mumbai"],
        ["Hyderabad","Delhi"],["Chennai","Kerala"]]
n = 4
start = "Bangalore"

res = main(paths,start)
print(res)

