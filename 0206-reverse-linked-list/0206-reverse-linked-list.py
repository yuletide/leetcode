# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #input head of linked list
        # output: reversed list
        # two methods: iterative or recursive

        # iterative method: while loop with counter
        # data store: LIFO = queue 
        # create a queue, iterate through the list push each node onto the queue, then pop off and reconstruct the list
        # O(n) storage O(n) runtime
        # recursive method: at the lowest level, to reverse a list we need two nodes at least, so we can build that unit, then recurse out
        # Reverse node(next node, current node) node.next = reverse(node, node.next)

        # if not head or not head.next:
        #     return head
        
        # de = deque([head])
        # current = head
        # while current.next:
        #     de.appendleft(current)
        #     current = current.next

        # linked list is like a stack
        newList = None

        while head:
            newList = ListNode(head.val, newList)
            head = head.next
        return newList

        # linked list reversal with recursion is not optimal in python

            
        
