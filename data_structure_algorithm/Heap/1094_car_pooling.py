import heapq
def carPooling( trips, capacity):
    trips.sort(key =lambda t:t[1])
    minheap = []
    curPass = 0
    for t in trips:
        numPass, start, end = t
        while minheap and minheap[0][0] <= start:
            curPass -= minheap[0][1]
            heapq.heappop(minheap)
        curPass += numPass
        if curPass > capacity:
            return False
        heapq.heappush(minheap,[end,numPass])
    return True