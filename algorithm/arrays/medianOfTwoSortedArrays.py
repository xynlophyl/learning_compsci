def findMedianSortedArrays(nums1, nums2):
  '''
  goal: given two sorted arrays, find the median of the combined array
  nums1: list[int], nums2: list[int]
  return: float
  '''
  n = len(nums1) + len(nums2)
  
  a, b = nums1, nums2
  if len(a) > len(b):
    a, b = b,a
    
  l, h = 0, len(a)-1
  while True:
    aMid = l + (h-l)//2
    bMid = n//2-aMid-2
    
    aLeft = a[aMid] if aMid > - 1 else float('-inf')
    aRight = a[aMid+1] if (aMid+1) < len(a) else float('inf')
    bLeft = b[bMid] if bMid > - 1 else float('-inf')
    bRight = b[bMid+1] if (bMid+1) < len(b) else float('inf')
    
    if aLeft <= bRight and bLeft <= aRight:
      if n%2:
        return min(aRight,bRight)
      return (max(aLeft,bLeft)+min(aRight,bRight))/2
    elif aLeft > bRight:
      h = aMid-1
    else:
      l = aMid + 1