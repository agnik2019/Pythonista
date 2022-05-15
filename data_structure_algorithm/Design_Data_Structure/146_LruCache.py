from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.size = capacity 

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.cache.move_to_end(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


'''

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.table = {}
        self.q = deque()
        
    def get(self, key: int) -> int:
        if key in self.table:
            self.q.remove(key)
            self.q.append(key)
            return self.table[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.q.remove(key)
        if len(self.q) == self.cap:
            del self.table[self.q.popleft()]
        self.q.append(key)  
        self.table[key] = value
'''