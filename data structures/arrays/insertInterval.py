def insert(intervals, newInterval):
	'''
	goal: insert newInterval into intervals such that there are no overlaps (there are no existing overlaps in intervals)
	intervals: list[list[int,int]], newInterval: list[int,int]
	return: list[list[int,int]]
	'''
	# optimized space: O(n) time, O(1) space
	if not intervals:
		return [newInterval]
	
	overlap = False
	added = False
	before_overlap = 0
	after_overlap = 1
	
	for i in range(len(intervals)):
		if not overlap:
			if newInterval[1] < intervals[i][0]:
				return intervals[:before_overlap]+[newInterval]+intervals[i:]
			elif not (newInterval[0] > intervals[i][1]):
				overlap = True
				newInterval = [min(newInterval[0], intervals[i][0]),max(newInterval[1],intervals[i][1])]
			else:
				before_overlap += 1
				after_overlap += 1
		else:
			if intervals[i][0] > newInterval[1]: # if interval starts later than new ends, then it is not overlappping 
				return intervals[:before_overlap]+ [newInterval] + intervals[i:]
			else:
				newInterval[1] = max(newInterval[1],intervals[i][1])
				after_overlap += 1
	
	return intervals[:before_overlap]+ [newInterval] + intervals[after_overlap:] 	# if exit loop without returning, then new has not been added yet

	
	
	# check each case: O(n) time, O(n) space
	if not intervals:
		return [newInterval]
	
	overlap = False # keeps track of whether newInterval is overlapped with last interval
	added = False # keeps track of whether newInterval has been added to the list
	ret = []

	for i in intervals:
		if overlap:
			if i[0] > newInterval[1]:
				overlap = False
				ret.append(newInterval)
				added = True
				ret.append(i)
			else:
				newInterval[1] = max(newInterval[1],i[1])

		else:
			if newInterval[1] < i[0]:
				if not added:
					ret.append(newInterval)
					added = True
				ret.append(i)
			elif newInterval[0] > i[1]:
				ret.append(i)
			else:
				if added:
					ret.append(i)
				else:
					overlap = True
					newInterval = [min(newInterval[0],i[0]),max(newInterval[1],i[1])]
	
	if not added:
		ret.append(newInterval)
	return ret
	