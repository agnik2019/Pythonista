from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        from collections import defaultdict
        adjlist = defaultdict(list)
        for s,d,w in flights:
            adjlist[s].append((d,w))
        queue = [(0,src,0)]  #stop,source,dist
        dist = [1e9]*n
        dist[src] = 0
        while queue:     
            nodedetails = queue[0]
            queue.pop(0)
            stops, node, cost = nodedetails[0],nodedetails[1],nodedetails[2]
            if stops > k: continue
            for neighbor in adjlist[node]:
                adjnode = neighbor[0]
                edw = neighbor[1]
                #print(f"{adjnode} -> {edw}")
                if cost+edw <dist[adjnode] and stops <= k:
                    dist[adjnode] = cost+edw
                    queue.append((stops+1,adjnode,cost+edw))
        #print(dist)
        if dist[dst] == 1e9: return -1
        return dist[dst]
            