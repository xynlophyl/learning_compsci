def majorityElement(nums):
    # Boyer-Moore Algorithm: O(n) time O(1) space
    count = 0
    candidate = 0
    for num in nums:
        if count == 0:
            candidate = num
        
        if candidate == num:
            count += 1
        else:
            count -= 1
    return candidate

    # divide and conquer: O(nlogn) time, O(log n) space 
    def helper(nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        majority_l = helper(nums[:n//2])
        majority_r = helper(nums[n//2:])
        if majority_l == majority_r:
            return majority_l
        
        count = 0
        if majority_l:
            for i in nums:
                if i == majority_l:
                    count += 1
            if count > n//2:
                return majority_l
        if majority_r:
            for i in nums:
                if i == majority_r:
                    count += 1
                if count > n//2:
                    return majority_r
        return None
    return helper(nums)

    # hash table: O(n) time, O(n) space
    n = len(nums)
    d = {}
    if n < 3:
        return nums[0]
    for i in nums:
        if i in d:
            if d[i]+1 >= n/2:
                return i
            else:
                d[i] += 1
        else:
            d[i] = 1
    