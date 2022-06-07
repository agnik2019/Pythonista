from heapq import *

class MedianOfStream:
    maxheap = []
    minheap = []
    def insert_num(self,num):
        if not self.maxheap or -self.maxheap[0] >= num:
            heappush(self.maxheap,-num)
        else:
            heappush(self.minheap,num)

        # either both the heaps will have equal no of elements
        # or maxheap will have one more element than the minheap
        if len(self.maxheap) > len(self.minheap)+1:
            heappush(self.minheap,-heappop(self.maxheap))
        if len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap,-heappop(self.minheap))

    def find_median(self):
        if len(self.minheap) == len(self.maxheap):
            return (-self.maxheap[0] + self.minheap[0])/2
        return -self.maxheap[0]


def main():
    mos = MedianOfStream()
    mos.insert_num(3)
    mos.insert_num(1)
    print(f"median of current stream {mos.find_median()}")
    mos.insert_num(5)
    print(f"median of current stream {mos.find_median()}")
    mos.insert_num(4)
    print(f"median of current stream {mos.find_median()}")


main()

