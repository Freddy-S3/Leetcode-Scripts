class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        if list2.val < list1.val:
            temp = list2
            list2 = list1
            list1 = temp
        
        prev = list1
        curr1 = list1.next
        curr2 = list2
        
        while curr1 != None or curr2 != None:
            if curr1 != None and curr2 != None:
                if curr1.val < curr2.val:
                    prev = prev.next
                    curr1 = curr1.next
                else:
                    temp = curr2
                    curr2 = curr2.next
                    prev.next = temp
                    temp.next = curr1
                    prev = prev.next

            elif curr1 == None and curr2 != None:
                prev.next = curr2
                return list1

            elif curr1 != None and curr2 == None:
                return list1
            
        return list1


"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.


Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""