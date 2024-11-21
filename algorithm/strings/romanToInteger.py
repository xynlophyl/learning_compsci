def romanToInt(s):
  '''
  goal: convert the roman numeral to decimal form
  s: str
  return: int
  '''
  convert = {
    'I': 1, 'V': 5,
    'X': 10, 'L': 50,
    'C': 100, 'D': 500,
    'M': 1000,
  }
  
  total = 0
  prev = 0
  for i in s:
      curr = convert[i]
      total += curr
      if prev < curr:
        total -= 2*prev
      prev = curr
  return total
      
      