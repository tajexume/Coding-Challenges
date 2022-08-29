"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for x in range(len(nums)):
            nums[x] = sum = sum + nums[x]
        return nums