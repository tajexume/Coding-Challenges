"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        upper = len(nums) - 1
        lower = 0
        med = lambda high, low: (high + low) // 2
        if len(nums) <= 2:
            if nums[lower] == target:
                return lower
            elif nums[upper] == target:
                return upper
        while lower <= upper:
            mid = med(upper,lower)
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                upper = mid-1
            elif nums[mid] < target:
                lower = mid + 1
            else:
                break
                
        if target > nums[upper]:
            return upper+1
        elif target < nums[lower]:
            return lower
