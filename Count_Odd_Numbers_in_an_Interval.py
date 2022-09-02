"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
"""

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        if high % 2 != 0 and low % 2 != 0:
            return int(diff / 2 + 1)
        elif high % 2 != 0 or low % 2 != 0:
            return int(diff // 2 + 1)
        else:
            return int(diff//2)
