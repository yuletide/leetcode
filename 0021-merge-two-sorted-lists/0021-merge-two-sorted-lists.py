# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # pointers on each list? 
        # start with lower value between head1, head2
        # while head1.next <= head2.next, add nodes from list 1
        # else, add nodes from list2
        # print("start", list1,list2)
        # if not list1 and not list2:
        #     return None
        # elif not list1:
        #     return list2
        # elif not list2:
        #     return list1

        # # set head to lesser value to start
        # head = list1 if list1.val <= list2.val else list2
        # last = head
        # while list1 or list2:
        #     print("iterating", last, list1, list2)
        #     if list1 and not list2:
        #         print("only list 1 remains")
        #         last.next = list1
        #         list1 = list1.next
        #         continue
            
        #     if list2 and not list1:
        #         print("only list 2 remains")
        #         last.next = list2
        #         last = list2
        #         list2 = list2.next
        #         continue
        #     # if we have both lists, add smaller node first
        #     if list1.val <= list2.val:
        #         print("list1 smaller")
        #         last.next = list1
        #         last = list1
        #         list1 = list1.next
        #     else:
        #         print("list2 smaller")
        #         last.next = list2
        #         last = list2
        #         list2 = list2.next
        # return head

        dummy = ListNode()
        head = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        
        if list1:
            # if only list 1 remains, tack it on
            head.next = list1
        elif list2:
            head.next = list2
        return dummy.next


