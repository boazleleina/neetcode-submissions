class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node (0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    #helper function to remove from end of list
    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    #helper function to insert to mru
    def _insert(self, node):
        prev, right = self.right.prev, self.right
        prev.next, node.next = node, right
        node.prev, right.prev = prev, node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
            
        return -1

    def put(self, key: int, value: int) -> None:
        #if the key is present then delete it first
        if key in self.cache:
            self._remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]       
