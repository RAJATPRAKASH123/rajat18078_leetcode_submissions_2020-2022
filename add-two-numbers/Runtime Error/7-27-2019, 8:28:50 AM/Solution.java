// https://leetcode.com/problems/add-two-numbers

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class ListNode
{
    int x;
    ListNode next;
    ListNode(int x )
    {
        this.x = x;
    }
}


public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode temp = l1;
        ListNode temp2 = l2;
        int papa = 0;int count1 = 0;
        int mama = 0;int count2 = 0;
        while( temp != null )
        {
            papa += temp.x * Math.pow(10,count1++);
        }
        while ( temp2 != null  )
        {
            mama += temp2.x * Math.pow(10, count2++);
        }
        ListNode node = new ListNode(mama + papa);
        return node;
    }
    
    public static void main(String[] args)
    {
        
    }
}