"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz = []
        for count in range(1,n + 1):
            if count % 3 == 0 and count % 5 == 0:
                fizz.append("FizzBuzz")
            elif count % 3 == 0:
                fizz.append("Fizz")
            elif count % 5 == 0:
                fizz.append("Buzz")
            else:
                fizz.append(str(count))
        return fizz