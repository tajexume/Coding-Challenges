"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        new_list = []
        hold = head
        while hold.next is not None:
            new_list.append(hold.val)
            hold = hold.next
        new_list.append(hold.val)
        n = new_list.copy()
        new_list.reverse()
        for number in range(len(new_list)):
            if new_list[number] == n[number]:
                continue
            else:
                return False
        return True