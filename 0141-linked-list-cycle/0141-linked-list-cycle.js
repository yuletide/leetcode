/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    let current = head
    let index = 0
    if (!current || !current.next){
        return false
    }
    while (current.next){
        current.pos = index;
        if (!current.next){
            return false
        }

        if (current.next.pos){
            return true
        }
        index++;
        current = current.next;

    }
    return false
    
};


// class Solution:
//     def hasCycle(self, head: Optional[ListNode]) -> bool:
//         visited = new 

//         index = 0
//         current = head

//         if head == None:
//             return False

//         while current.next:
//             # print(current.val)
//             if not current.next:
//                 return False
//             if current.next in visited:
//                 return True
//             visited.append(current)
//             current = current.next    
//             # self.hasCycle(head.next)
