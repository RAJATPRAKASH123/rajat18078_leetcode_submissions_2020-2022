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
        ListNode res = new ListNode(0);
        ListNode temp = res;
        int c = 0;
        while( a != null || b != null )
        {
            int x = a != null ? a.val : 0 ;
            int y = b != null ? b.val : 0;
            int ans = x + y + c;
            c = ans/10;
            ListNode kk = new ListNode(ans%10);
            //System.out.println(ans%10);
            temp.next = kk;
            temp = temp.next;
            if ( a != null )
            {
                a = a.next;
            }
            if ( b != null )
            {
                b = b.next;
            }
        }
        return res.next;
    }
}