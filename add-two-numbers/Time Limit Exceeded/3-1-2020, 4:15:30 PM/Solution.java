// https://leetcode.com/problems/add-two-numbers

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode a = l1;
        ListNode b = l2;
        int carry = 0;
        int ans = 0;
        int mul = 0;
        while( a != null && b != null )
        {
            ans += (a.val + b.val) * Math.pow(10,mul++) ;
            a = a.next; b = b.next;
        }
        while( b != null )
        {
            ans += b.val * Math.pow(10,mul++);
        }
        while( a != null )
        {
            ans += a.val * Math.pow(10,mul++);
        }
        ListNode l = new ListNode(ans%10);
        ListNode t = l;
        ans /= 10;
        while ( ans != 0 )
        {
            ListNode temp = new ListNode(ans%10);
            t.next = temp;
            ans /= 10;
            t = t.next;
        }
        return l;
    }
}