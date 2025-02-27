// https://leetcode.com/problems/reverse-linked-list

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        // if ( head == null )
        // {
        //     return null;
        // }
        // if ( head.next == null )
        // {
        //     return head;
        // }
        // ListNode prev = null;
        // ListNode cur = head;
        // ListNode next = null;
        // while ( cur != null )
        // {
        //     next = cur.next;
        //     cur.next = prev;
        //     prev = cur;
        //     cur = next; 
        // }
        // head = prev;
        // return head;
        if ( head == null || head.next == null )
        {
            return head;
        }
        ListNode p = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return p;   
    }
}