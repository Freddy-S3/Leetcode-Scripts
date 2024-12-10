class Solution(object):
    def addTwoNumber(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = l1
        list1 = l1
        list2 = l2
        prev = None
        
        while list1 != None and list2 != None:
            
            list1.val = list1.val + list2.val + carry
            
            if list1.val >= 10:
                carry = 1
                list1.val = list1.val % 10
            else:
                carry = 0
            
            prev = list1
            list1, list2 = list1.next, list2.next
        
        
        if list1 == None:
            prev.next = list2
            
            list1 = list2
        
        
        while carry == 1 and list1 != None:
            
            list1.val = list1.val + carry
            
            if list1.val >= 10:
                carry = 1
                list1.val = list1.val % 10
            else:
                carry = 0
            
            prev = list1
            list1 = list1.next
            
        
        if carry == 1:
            prev.next = ListNode(1)

        
        return head
    
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None   
    
    


"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
 Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""