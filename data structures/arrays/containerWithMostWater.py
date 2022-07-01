def maxArea(height):
    # greedy height and area while shrinking width: O(n) time, O(1) space
    low = 0
    high = len(height)-1
    area = 0
    last_highest = [0,0]
    
    while low < high:
        curr = min(height[low],height[high])*(high-low)
        area = max(curr,area)
        if height[low] > height[high]:
            high -= 1
        else:
            low += 1
    return area