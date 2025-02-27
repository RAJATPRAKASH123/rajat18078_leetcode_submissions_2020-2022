// https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        if not head.next.next:
            return head
        last = head
        count = 0
        while last.next:
            last = last.next
            count += 1
        cur_last = last
        temp = head
        while temp and temp != last and temp.next != last:
            apnd_node = temp.next
            temp.next = temp.next.next
            
            cur_last.next = apnd_node
            apnd_node.next = None
            cur_last = cur_last.next
            
            temp = temp.next
        if temp.next == last:
            even_last = last
            temp.next = temp.next.next
            even_last.next = None
            cur_last.next = even_last
        # if temp.next == last:
        #     last.next = None
        #     cur_last.next = last
        # # if count%2 == 0:
        # #     # temp.next = None
        # #     # cur_last.next = tem
        return head