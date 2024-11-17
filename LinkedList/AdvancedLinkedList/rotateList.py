class Solution(object):
    def rotateRight(self, head, k):
        if head == None or head.next == None:
            return head
        curr = head
        counter = 1
        
        while curr.next != None:
            curr = curr.next
            counter += 1
        
        end = curr
        rotate = k % counter
        
        if rotate == 0:
            return head
        
        newEnd = counter - rotate - 1
        curr = head

        for i in range(newEnd):
            curr = curr.next
        
        newHead = curr.next
        curr.next = None
        end.next = head
        head = newHead
        
        return head
        
                   

"""
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""