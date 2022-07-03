def longestOnes_One(nums):
    # track max: O(n) time, O(1) space
	max_count = 0
	count = 0
	
	for i in nums:
		if i == 1:
			count += 1
		else:
			count = 0
		max_count = max(count,max_count)
	return max_count

def longestOnes_Two(nums):
	pass
 
def longestOnes_Three(nums, k):
	# more efficient sliding window, no inner while loop: O(n) time, O(1) space
	low = 0
	for high in range(len(nums)):
		if nums[high] == 0:
			k -= 1
		if k < 0:
			if nums[low] == 0:
				k += 1
			low += 1
	return high-low+1

	# sliding window, record most possible ones in a row: O(n) time, O(1) space
	count = low = flipped = 0
	for high in range(len(nums)):
		if nums[high] == 0: 
			flipped += 1
		while flipped > k:
			if nums[low] == 0: 
				flipped -= 1
			low += 1
		count = max(count,high-low+1)
	return count