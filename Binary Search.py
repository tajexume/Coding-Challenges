"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        
        return -1
