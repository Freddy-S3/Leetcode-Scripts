package LinkedList.AdvancedLinkedList;

public class merge2SortedLists {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) return list2;
        if (list2 == null) return list1;
        ListNode temp = list1;
        if (list2.val < list1.val){
            list1 = list2;
            list2 = temp;
        }
        
        ListNode prev = list1;
        ListNode curr1 = list1.next;
        ListNode curr2 = list2;
        
        while (curr1 != null || curr2 != null){
            if (curr1 != null && curr2 != null){
                if (curr1.val < curr2.val){
                    prev = prev.next;
                    curr1 = curr1.next;
                }
                
                else{
                    temp = curr2;
                    curr2 = curr2.next;
                    
                    prev.next = temp;
                    prev = prev.next;
                    prev.next = curr1;
                }
                            
            }
            else if(curr1 == null){
                prev.next = curr2;
                return list1;
            }
            
            else if(curr2 == null){
                return list1;
            }

        }
        return list1;
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

/*
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
 */