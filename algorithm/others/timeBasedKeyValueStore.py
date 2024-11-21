class TimeMap:
  '''
  goal: create a key-value map class where pairs can be stored and called at different timestamps
  key: str, value: str, timestamp: int

  '''
  def __init__(self):
    self.dict = {}
    
  def set(self, key, value, timestamp):
    # since timestamps are strictly increasing at each call, each (t, v) pair is sorted in ascending order already
    if key in self.dict:
      self.dict[key].append((timestamp, value))
    else:
      self.dict[key] = [(timestamp, value)]
    
  def get(self, key, timestamp):
    vals = self.dict.get(key, [])
    
    low, high = 0, len(vals) - 1
    last = ''
    while low <= high:
      mid = low + (high-low)//2
      if vals[mid][0] == timestamp:
        return vals[mid][1]
      elif vals[mid][0] < timestamp:
        last = vals[mid][1]
        low = mid + 1
      else:
        high = mid - 1
    return last
