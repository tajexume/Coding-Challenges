"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower = 1
        upper = n
        med = lambda high, low: (high + low) // 2
        if n == 1:
            return n
        while lower <= upper:
            mid = med(upper,lower)
            if isBadVersion(mid) and isBadVersion(mid-1) is False:
                return mid
            elif isBadVersion(mid) and isBadVersion(mid-1):
                upper = mid-1
            elif isBadVersion(mid) is False:
                lower = mid + 1
        return 0
            
