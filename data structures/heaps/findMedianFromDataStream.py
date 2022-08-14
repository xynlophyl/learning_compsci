'''
goal: design a class that is able to input a datastream and determine the median of all the elements so far
'''

import heapq
class MedianFinder:

  def __init__(self):
    self.minHeap = []
    self.maxHeap = []

  def addNum(self, num: int) -> None:
    if not self.minHeap or not self.maxHeap:
      heapq.heappush(self.minHeap, num)
    else:
      val = -self.maxHeap[0] if self.maxHeap else float('inf')
      if num > val:
        heapq.heappush(self.minHeap, num)
      else:
        heapq.heappush(self.maxHeap, -num)
    if len(self.minHeap) > len(self.maxHeap) + 1:
      curr = heapq.heappop(self.minHeap)
      heapq.heappush(self.maxHeap, -curr)
    elif len(self.maxHeap) > len(self.minHeap) + 1:
      curr = -heapq.heappop(self.maxHeap)
      heapq.heappush(self.minHeap, curr)

  def findMedian(self) -> float:
    if len(self.minHeap) > len(self.maxHeap):
      return self.minHeap[0]
    elif len(self.minHeap) < len(self.maxHeap):
      return -self.maxHeap[0]
    else:
      return (self.minHeap[0] - self.maxHeap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
