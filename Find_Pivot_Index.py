class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Sum = sum(nums)
        for x in range(len(nums)):
            left_sum = sum(nums[:x])
            right_sum = Sum - left_sum - nums[x]
            if left_sum == right_sum:
                return x
        return -1
