def merge(intervals):
	'''
	goal: merge each interval in intervals such that there are no overlaps in the result
	intervals: list[list[int,int]]
	return: list[list[int,int]]
	'''
	# sort then merge by comparison: O(nlogn) time, o(n) space
	intervals.sort(key=lambda x:x[0])
	new_intervals = [intervals[0]]
	
	for i in range(1,len(intervals)):
		last = new_intervals.pop()
		if intervals[i][0] <= last[1]:
			new_intervals.append([last[0], max(intervals[i][1],last[1])])
		else:
			new_intervals.append(last)
			new_intervals.append(intervals[i])
	return new_intervals
	