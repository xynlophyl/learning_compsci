def productExceptSelf(nums):
	'''
	goal: return a list where each index,i, is the product of nums excluding nums[i]
	nums: list[int]
	return: list[int] 
	'''
    # track 0 and total product, multiple passes: O(n) time, O(n) space
	zero_count = 0
	product = 1
	for i in nums:
		if i == 0:
			zero_count += 1
		else:
			product*=i
	if zero_count > 1:
		return [0 for i in nums]
	
	if zero_count==0:
		return [product//i for i in nums]
	
	answer = []
	for i in nums:
		if i == 0:
			answer.append(product)
		else:
			answer.append(0)
	return answer
