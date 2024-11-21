def calculate(s):
  '''
  goal: design a string that can parse simple addition and subtract expressions
  s: string
  return: int
  '''
  nums, opers= [], []
  currNum, sign = '0', 1
  currSum = 0
  for i in s:
    if i.isdigit():
      currNum += i
    elif i in '+-':
      currSum += int(currNum)*sign
      currNum = '0'
      sign = 1 if i == '+' else -1
    elif i == '(':
      nums.append(currSum)
      opers.append(sign)
      currSum = 0
      sign = 1
    elif i == ')':
      currSum += int(currNum)*sign
      currSum *= opers.pop()
      currSum += nums.pop()
      currNum = '0'

  return currSum + (int(currNum)*sign)
