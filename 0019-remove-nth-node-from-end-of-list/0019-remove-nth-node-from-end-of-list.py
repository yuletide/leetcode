# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # input: head of list
        # output: head of list with nth node removed
        # we can't get length of the list, but we can traverse with two pointers
        # left pointer is the tortoise, starting at head
        # right pointer is the hare, starting at head + n

        turtle = head
        hare = head
        carrots = n
        prev = None

        if not head.next:
            return None

        while carrots:
            hare = hare.next
            carrots -= 1

        while hare:
            hare = hare.next
            prev = turtle
            turtle = turtle.next
        
        # delete the node
        if not prev:
            return turtle.next

        prev.next = prev.next.next
        return head

        
        