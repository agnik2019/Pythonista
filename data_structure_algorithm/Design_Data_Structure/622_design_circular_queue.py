class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [0]*k
        self.head = 0
        self.tail = -1
        self.maxsize = k 
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.maxsize: return False
        if self.tail == -1:
            self.head = self.tail = 0
        else:
            self.tail = (self.tail+1)% self.maxsize
        self.data[self.tail] = value
        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        if self.size == 0: return False
        if self.head == self.tail:
            self.head = self.tail = -1
        self.head = (self.head+1)% self.maxsize
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.data[self.head] if self.size != 0 else -1

    def Rear(self) -> int:
        return self.data[self.tail] if self.size != 0 else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxsize
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()