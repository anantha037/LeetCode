class Node:
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}
        self.left, self.right = Node(0,0),Node(0,0)
        self.left.next, self.right.prev = self.right,self.left
    
    def add(self,node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next,self.right.prev = self.right,node
    def remove(self,node):
        nxt, prev = node.next, node.prev
        prev.next,nxt.prev = nxt,prev
    def get(self, key: int) -> int:
        if key in self.table:
            node = self.table[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.remove(self.table[key])
        self.table[key] = Node(key,value)
        self.add(self.table[key])
        
        if len(self.table)>self.capacity:
            # print(key,value,self.table)
            last = self.left.next
            self.remove(last)
            del self.table[last.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)