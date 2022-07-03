def firstMissingPositive(nums):
	# negative marking: O(n) time and O(1) space
	if not nums: return 1
	
	n = len(nums)
	one_flag = True
	
	for i in range(n):
		curr = nums[i]
		if curr == 1: one_flag = False
		elif curr <= 0 or curr > len(nums):  
			nums[i] = 1 # changes all negative numbers and numbers outside range of list to 1, since the original numbers are not part of the algorithm and 1 has already been searched for
	if one_flag: 
		return 1 #there is no 1 in the array, so return 1

	for j in range(n):
		val = abs(nums[j])-1
		if nums[val] > 0:
			nums[val] = -1*nums[val] #negating the value at index val to indicate that val has been seen
	for k in range(n):
		if nums[k] > 0:
			return k+1 #if value at index i is still positive, then that means i+1 is missing
	return n+1

	# using memory: O(n) time and O(n) space
	d = set()
	
	for i in nums:
		if i not in d:
			d.add(i)
	
	for i in range(1,len(nums)+1):
		if i not in d:
			return i
	return len(nums)+1
