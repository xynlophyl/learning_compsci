def evalRPN(tokens):
  '''
  goal: evaluate the value of the given arithmetic expression using Reverse Polish Notation
  tokens: list[str]
  return: int
  '''
  oper = '+-*/'
  stack = []
  for t in tokens:
    if t == '+':
      stack.append(stack.pop()+stack.pop())
    elif t == '-':
      x = stack.pop()
      y = stack.pop()
      stack.append(y-x)
    elif t == "*":
      stack.append(stack.pop()*stack.pop())
    elif t == '/':
      x = stack.pop()
      y = stack.pop()
      stack.append(int(y/x))
    else:
      stack.append(int(t))
  return stack[0]
  