# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        index = 0
        current = head

        if head == None:
            return False

        while current.next:
            # print(current.val)
            if not current.next:
                return False
            if current.next in visited:
                return True
            visited.append(current)
            current = current.next    
            # self.hasCycle(head.next)
