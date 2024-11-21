def rotate(nums, k):
	'''
	goal: shift nums by k elements to the right
	nums: list[int], k: int
	return: list[int]
	'''
	# reverse individual slices: O(n) time, O(1) space 
	def reverse(nums,l,r):
		while l < r:
			nums[l], nums[r] = nums[r], nums[l]
			l += 1
			r -= 1
	n = len(nums)
	k = k%n 
	reverse(nums,0,n-1) # reverses entire list
	reverse(nums,0,k-1) # splits array w/ cut off at k, then reverses each slice inidividually
	reverse(nums,k,n-1) 
	return nums
	
	# forceful switch: O(n) time, O(n) space
	n = len(nums)
	mod = k%len(nums)
	if mod:
		nums[:mod], nums[mod:] = nums[n-mod:], nums[:n-mod]
	return nums
	
	
	# simulation: O(n) time, O(1) space [DOESNT MEET TIME REQUIREMENTS]
	mod = k%len(nums)
	if mod:
		for _ in range(mod):
			nums[0], nums[1:] = nums[-1], nums[0:-1]
	
	return nums
	