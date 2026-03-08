#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class CacheNode:

    def __init__(self, _key: int = 0, _prev: CacheNode = None, _next: CacheNode = None):
        self.key = _key
        self.prev = _prev
        self.next = _next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.lru_list_head = CacheNode()
        self.lru_list_tail = CacheNode()

        self.lru_list_head.next = self.lru_list_tail
        self.lru_list_tail.prev = self.lru_list_head

    def _insert_to_recent_used(self, node: CacheNode):
        node.prev = self.lru_list_tail.prev
        node.next = self.lru_list_tail
        self.lru_list_tail.prev.next = node
        self.lru_list_tail.prev = node

        
    def get(self, key: int) -> int:
        if key not in self.cache or len(self.cache) == 0:
            return -1
        
        val, node = self.cache[key]

        if node != self.lru_list_tail.prev:
            node.prev.next = node.next
            node.next.prev = node.prev

            self._insert_to_recent_used(node)

        return val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = CacheNode(key)

            self._insert_to_recent_used(node)

            self.cache[key] = (value, node)
        else:
            _, node = self.cache[key]
            
            if node != self.lru_list_tail.prev:
                node.prev.next = node.next
                node.next.prev = node.prev

                self._insert_to_recent_used(node)

            self.cache[key] = (value, node)

        if len(self.cache) > self.capacity:
            evict_node = self.lru_list_head.next
            self.lru_list_head.next = evict_node.next
            evict_node.next.prev = self.lru_list_head

            del self.cache[evict_node.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

