"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Sum = sum(nums)
        for x in range(len(nums)):
            left_sum = sum(nums[:x])
            right_sum = Sum - left_sum - nums[x]
            if left_sum == right_sum:
                return x
        return -1
