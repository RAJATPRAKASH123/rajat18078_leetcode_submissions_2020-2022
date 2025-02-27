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
        long ans = 0;
        long mul = 0;
        while( a != null && b != null )
        {
            ans += (a.val + b.val) * Math.pow(10,mul++) ;
            a = a.next; b = b.next;
        }
        while( b != null )
        {
            ans += b.val * Math.pow(10,mul++);
            b = b.next;
        }
        while( a != null )
        {
            ans += a.val * Math.pow(10,mul++);
            a = a.next;
        }
        int md =(int) (ans%10);
        ListNode l = new ListNode(md);
        ListNode t = l;       
        ans /= 10;
        //System.out.println(ans);
        while ( ans != 0 )
        {
            int mdd =(int) (ans%10);
            ListNode temp = new ListNode(mdd);
            t.next = temp;
            ans /= 10;
            t = t.next;
        }
        return l;
    }
}