'''
goal: design a stack that returns the most recently added value with the highest frequency 
'''

class FreqStack:

  def __init__(self):
    self.stack = {}
    self.counts = {}
    self.max_count = 0
  def push(self, val: int) -> None:
    count = self.counts.get(val, 0) + 1
    self.counts[val] = count
    if count > self.max_count:
      self.max_count = count
      self.stack[count] = []
    self.stack[count].append(val)
  def pop(self) -> int:
    stack = self.stack[self.max_count]
    res = stack.pop()
    self.counts[res] -= 1
    if not stack:
      self.max_count -= 1
    return res
    
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
