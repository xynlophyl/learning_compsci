def sortColors(nums):
	# single pass: O(n) time, O(1) space
	low = 0
	high = len(nums)-1
	i = 0
	while i <= high:
		if nums[i] == 0:
			nums[i], nums[low]  = nums[low], nums[i]
			low += 1
		elif nums[i] == 2:
			nums[i], nums[high] = nums[high], nums[i]
			i -= 1
			high -= 1
		i += 1
	return nums
	# memory: O(n) time, O(n) space
	
	d = {0:0,1:0,2:0}
	
	for color in nums:
		d[color] += 1
			
	n = 0
	for i in d:
		for j in range(d[i]):
			nums[n+j] = i
		n += d[i]
	return nums
	