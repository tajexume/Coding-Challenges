"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        counter = 0
        while node.next is not None:
            node = node.next
            counter += 1
        node = head
        for count in range(counter):
            if count is not math.ceil(counter/2):
                node = node.next
            else:
                return node
        
        return node