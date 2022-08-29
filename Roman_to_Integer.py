"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        checker = False
        values = {'I': 1,
                  'IV': 4,
                 'V': 5,
                 'IX': 9,
                 'X': 10,
                 'XL': 40,
                 'L': 50,
                 'XC': 90,
                 'C': 100,
                 'CD': 400,
                 'D': 500,
                 'CM': 900,
                 'M': 1000}
        for roman in range(len(s)):
            if(checker is False):
                if(roman != len(s) - 1):
                    if(s[roman] == 'I' and s[roman + 1] == 'V'):
                        total += values['IV']
                        checker = True
                    elif(s[roman] == 'I' and s[roman + 1] == 'X'):
                        total += values['IX']
                        checker = True
                    elif (s[roman] == 'X' and s[roman + 1] == 'L'):
                        total += values['XL']
                        checker = True
                    elif (s[roman] == 'X' and s[roman + 1] == 'C'):
                        total += values['XC']
                        checker = True  
                    elif (s[roman] == 'C' and s[roman + 1] == 'D'):
                        total += values['CD']
                        checker = True
                    elif (s[roman] == 'C' and s[roman + 1] == 'M'):
                        total += values['CM']
                        checker = True
                    else:
                        total += values[s[roman]]
                else:
                    total += values[s[roman]]
            else:
                checker = False
        return total
        