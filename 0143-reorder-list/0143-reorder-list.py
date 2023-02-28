# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # node 0 -> node n -> node 1 -> node n-1 -> node 2 -> node n-2

        # n = 4
        # 1 -> 4 -> 2 -> 3
        # go until i = n
        # left pointer = head
        # right pointer = tail


        # approach: loop through entire list and store in a data structure -> LIFO
        # loop through list again and insert nodes from end until we meet
        # recursion could also work

        # First attempt
        # dummy = ListNode()
        # nodeStack = deque([]) # might not be needed if we use two pointers
        # dummy.next = head
        # l = head
        # r = head
        # lnext = None
        # length = 1
        # while r.next:
        #     nodeStack.append(r)
        #     r = r.next
        #     length += 1
        # print("length", length, l.val,r.val)
        # print(nodeStack)
        # i = 0
        # while i < length:
        #     #save pointer to next node in order (2)
        #     lnext = l.next
        #     #point head to last node (4)
        #     l.next = nodeStack[-1]
        #     nodeStack.pop()
        #     l = l.next
        #     i += 1
        #     # point last node (now second node) to previous second node
        #     l.next = lnext
        #     l = l.next
        #     i += 1
        #     print(i)
        # print(dummy)
        # return dummy.next

        # if not head.next:
        #     return head
        
        # start = head
        # stack = []
        # while start.next:
        #     stack.append(start.next)
        #     start = start.next
        # print(len(stack))
        
        # end_len = math.ceil(len(stack)/2)
        # prev_node = head
        # print(end_len)
        # while len(stack) > end_len:
        #     print("looping")
        #     end_node = stack.pop()
        #     prev_node.next = end_node
        # return head



        # QUEUE SOLUTION
        # pointer to result node to return
        result = ListNode()
        # tail node to use for appending
        tail = result
        q = deque()
        curr = head
        while curr:
            q.append(curr)
            curr = curr.next
        
        while q:
            left = q.popleft()
            tail.next = left
            tail = tail.next
            if q:
                right = q.pop()
                tail.next = right
                tail = tail.next
            tail.next = None
        return result.next


        


        