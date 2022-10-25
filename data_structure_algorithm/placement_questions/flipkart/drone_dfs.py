# 5 3
# 1 2
# 1 3
# 3 4
# 3 5
# 5 6

from collections import defaultdict


# m,n = map(int,input().split())
# nodes = []

# for _ in range(m):
#     nodes.append(list(map(int,input().split())))
nodes = [[1, 2], [1, 3], [3, 4], [3, 5], [5, 6]]
nodeset = set()
adj_list = defaultdict(list)
for n in nodes:
    nodeset.add(n[0])
    nodeset.add(n[1])
noofnode = len(nodeset)
adjmat = [[-1]*noofnode for _ in range(noofnode)]
for i in range(noofnode):
    for j in range(noofnode):
        if i==j: adjmat[i][j] = 0
        else:
            adjmat[i][j] = 9999

for n in nodes:
    adjmat[n[0]-1][n[1]-1]  = 1
    adjmat[n[1]-1][n[0]-1] = 1

for k in range(0,noofnode):
    for i in range(0,noofnode):
        for j in range(0,noofnode):
            adjmat[i][j] = min(adjmat[i][j], adjmat[i][k]+adjmat[k][j])


for i in range(0,noofnode):
    for j in range(0,noofnode):
        print(adjmat[i][j], end=" ")
    print()
cnt = 0
for i in range(0,noofnode):
    for j in range(0,noofnode):
        if adjmat[i][j] == 3:
            cnt += 1
        
print(cnt//2)
