"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 1
        node = head
        if head.next is None:
            return None
        else:
            while node.next != None:
                sz += 1
                node = node.next
                
            node = head
            if 0 == sz - n:
                head = head.next
                return head
            elif 1 == n:
                while node.next.next is not None:
                    node = node.next
                node.next = None
                return head
            else:
                count = 1
                while node is not None:
                    if count == sz - n:
                        node.next = node.next.next
                        return head
                    count += 1
                    node = node.next
            return head