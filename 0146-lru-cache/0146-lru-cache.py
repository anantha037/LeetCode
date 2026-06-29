class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}
        self.length = 0
        self.least_used = deque()

    def get(self, key: int) -> int:
        # print(self.table)
        if key in self.table:
            self.least_used.append(key)
        return self.table.get(key,-1)

    def put(self, key: int, value: int) -> None:
        if key not in self.table:
            self.length+=1
        if self.length>self.capacity:
            # print('hello',self.least_used)
            c = self.least_used.popleft()
            while c in self.least_used:
                # print('hi',self.least_used)
                c = self.least_used.popleft()
            # print('hoi',self.least_used)
            del self.table[c]
            self.length-=1
        # print(self.least_used,self.table)
        self.table[key]=value
        self.least_used.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)