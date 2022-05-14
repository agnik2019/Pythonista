class heappq:
    def __init__(self,array):
        self.heap = self.buildHeap(array)
        self.size = 0
    
    def leftChild(self,i):
        return 2*i + 1
    
    def rightChild(self,i):
        return 2*i + 2
    
    def parent(self,i):
        return (i-1)//2

    def siftUp(self,heap,currentIdx):
        parentIdx = self.parent(currentIdx)
        if currentIdx>0 and heap[currentIdx] > heap[parentIdx]:
            heap[currentIdx], heap[parentIdx] = heap[parentIdx],heap[currentIdx]
            currentIdx = parentIdx
            parentIdx = self.parent(currentIdx)
    
    def siftDown(self,heap, i):
        l = self.leftChild(i)
        r = self.rightChild(i)
        smallest = i
        size = len(heap) - 1
        if l < size and heap[l] < heap[smallest]:
            smallest = l
        if r < size and heap[r] < heap[smallest]:
            smallest = r
        if smallest != i:
            heap[smallest], heap[i] = heap[i], heap[smallest]
            self.siftDown(heap,smallest)

    def heappush(self,item):
        self.heap.append(item)
        self.siftUp(self.heap,len(self.heap)-1)

    def heappop(self):
        self.heap[0],self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1],self.heap[0]
        valueToRemove = self.heap.pop()
        self.siftDown(self.heap,0)
        return valueToRemove

    def buildHeap(self,array):
        n = int((len(array)//2)-1)
        for k in range(n, -1, -1):
            self.siftDown(array,k)
        return array



l = [4,5,2,13,54,23]
hp = heappq(l)
hp.heappush(44)
print(l)  # [2, 5, 44, 13, 54, 23, 4]
hp.heappop()
print(l)  # [4, 5, 44, 13, 54, 23]