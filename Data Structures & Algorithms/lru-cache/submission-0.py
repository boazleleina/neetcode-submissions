class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        #rewire neighbors to bypass it
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_front(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        next_node.prev = node
        node.next = next_node

    def get(self, key: int) -> int:
        #check if the value is in the cache
        if key in self.cache:
            self._remove(self.cache[key])
            self._add_to_front(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        else:
            self.cache[key] = Node(key, value)
            self._add_to_front(self.cache[key])
            if (len(self.cache)) > self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            
