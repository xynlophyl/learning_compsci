'''
goal: design a queue using 2 stacks
'''
class MyQueue:

  def __init__(self):
    self.pushStack = []
    self.popStack = []

  def push(self, x):
    # return self.push_linear
    return self.push_constant
  
  def pop(self, x):
    # return self.pop_constant(x)
    return self.pop_amortized_linear(x)

  def peek(self):
    # return self.peek_1
    return self.peek_2

  def empty(self):
    return not (self.popStack or self.pushStack)
    

  # repopulating pop stack every push: O(n) push, O(1) pop
  def push_linear(self, x: int) -> None:
    if self.popStack:
      while self.popStack:
        self.pushStack.append(self.popStack.pop())
    self.pushStack.append(x)
    
    while self.pushStack:
      self.popStack.append(self.pushStack.pop())
    return

  def pop_constant(self):
    return self.popStack.pop()

  def peek_1(self):
    return self.popStack[-1]

  # pushing to push stack and repopulating pop stack when it is empty: O(1) push, amortized O(n) pop 
  def push_constant(self, x):
    if not self.pushStack:
      self.front = x
    self.pushStack.append(x)

  def pop_amortized_linear(self):
    if not self.popStack:
      while self.pushStack:
        self.popStack.append(self.pushStack.pop())
    return self.popStack.pop()

  def peek_2(self):
    return self.popStack[-1] if self.popStack else self.front
    



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()