package LinkedList.AdvancedLinkedList;

public class rotateList {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) return head; 
        
        int counter = 1;
        ListNode endNode = head;
        while (endNode.next != null){
            endNode = endNode.next;
            counter++;
        }

        if (k % counter == 0) return head;
        
        ListNode newEnd = head;
        for (int i = counter - (k % counter) - 1; i>0; i--) newEnd = newEnd.next;
        
        ListNode newHead = newEnd.next;
        newEnd.next = null;
        endNode.next = head;
        head = newHead;
        
        return head;
    }
}

/*
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
 */