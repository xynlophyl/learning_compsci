'''
goal: design a Least Recently Used Cache, where it stores a fixed number of key-value pairs and evicts the least recently used pair
'''
class ListNode:
  def __init__(self, key=-1, val=-1, nxt=None, prev=None):
    self.key = key
    self.val = val
    self.prev = prev
    self.next = nxt

class LRUCache:

  def __init__(self, capacity: int):
    self.d = {}
    self.capacity = capacity
    self.n = 0
    
    self.head, self.tail = ListNode(), ListNode()
    self.head.next, self.tail.prev = self.tail, self.head
          
  def get(self, key: int) -> int:
    node = self.d.get(key, ListNode())
    if node.key != -1:
      self.pop(node)
      self.append(node)
      
    # print(key, node.val, self.print_list())
    return node.val

  def put(self, key: int, value: int) -> None:
    if key in self.d and self.d[key].val != -1:
      self.pop(self.d[key])
      self.n -= 1
    self.d[key] = ListNode(key=key, val=value)
    self.append(self.d[key])
    self.n += 1
    
    if self.n > self.capacity:
      lru = self.head.next
      self.pop(lru)
      self.d[lru.key] = ListNode()
      self.n -= 1
    
  def pop(self, node):
    prev, nxt = node.prev, node.next
    prev.next, nxt.prev = nxt, prev
  
  def append(self, node):
    prev, nxt = self.tail.prev, self.tail
    prev.next = nxt.prev = node
    node.next, node.prev = nxt, prev
    
  def print_list(self):
    curr = self.head
    l = []
    while curr:
      l.append((curr.key, curr.val))
      curr = curr.next
    return l

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
