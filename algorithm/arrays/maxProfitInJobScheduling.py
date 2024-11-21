def jobScheduling(startTime, endTime, profit):
  '''
  goal: find the schedule from the given jobs that returns the max profit, where there are no overlaps in times between the used jobs  
  startTime: list[int], endTime: list[int], profit: list[int]
  return: int
  '''
  n = len(startTime)
  def sortJobs(start, end, profit):
    jobs = sorted([(start[i], end[i], profit[i]) for i in range(n)]) 
    return jobs
  
  def binarySearch(jobs, low, target):
    high = n-1
    last = -1
    while low <= high:
      mid = low + (high-low)//2
      if jobs[mid][0] == target:
        return mid
      elif jobs[mid][0] > target:
        last = mid
        high = mid - 1
      else: 
        low = mid + 1
    return last
        
  jobs = sortJobs(startTime, endTime, profit) # groups + sorts times and profit of jobs by start time
  lastJob = [binarySearch(jobs,i, jobs[i][1]) for i in range(n)] # finds last job that finishes before current jobs starts
  opt = [-1 for i in range(n)] # finds the max profit
  opt[-1] = jobs[-1][2]
  
  for i in range(n-2, -1, -1):
    if lastJob[i] == -1:
      prev = 0
    else:
      prev = opt[lastJob[i]]
    
    opt[i] = max(opt[i+1], jobs[i][2] + prev)
  return opt[0]
  