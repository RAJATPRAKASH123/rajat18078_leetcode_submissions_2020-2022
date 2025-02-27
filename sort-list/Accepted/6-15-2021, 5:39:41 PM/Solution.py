// https://leetcode.com/problems/sort-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        def merge(first, sec):
            if not first:
                return sec
            if not sec:
                return first
            if first.val < sec.val:
                first.next = merge(first.next, sec)
            else:
                first, sec = sec, first
                first.next = merge(first.next, sec)
            return first
            
        def mergeSort(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head
            prev = slow
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
            prev.next = None
            return merge(mergeSort(head), mergeSort(slow))
        return mergeSort(head)
    
'''
1 4 9 13
2 7 15 16

1 2
4
class Solution 
{
public:
    ListNode *merge_two(ListNode *first,ListNode *second)
    {
        if(!first)
        {
            return second;
        }
        if(!second)
        {
            return first;
        }
        if(first->val>second->val)
        {
            return merge_two(second,first);
        }
        first->next=merge_two(first->next,second);
        return first;
    }
    ListNode* sortList(ListNode* head)
    {
        if(!head || !head->next)
        {
            return head;
        }
        ListNode *slow=head,*fast=head,*tmp=head;
        while(slow && fast && fast->next)
        {
            slow=slow->next;
            fast=fast->next->next;
        }
        while(tmp && tmp->next && tmp->next!=slow)
        {
            tmp=tmp->next;
        }
        tmp->next=NULL;
        ListNode *first=sortList(head);
        ListNode *second=sortList(slow);
        ListNode *ans=merge_two(first,second);
        return ans;
    }
};
'''