#recursive
class Solution(object):
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node

"""
#itterative
class Solution(object):
    def reverseList(self, head):
        prev = None
        while head != None:
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev
"""

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. 
Could you implement both?
"""