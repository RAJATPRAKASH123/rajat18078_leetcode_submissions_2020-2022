// https://leetcode.com/problems/next-greater-node-in-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        prev = None
        cur = head
        nxt = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # head of reversed linkedlist : rev
        rev = prev
        stack = deque([float('inf')]); res = deque()
        while rev:
            while stack:
                if stack[0] <= rev.val:
                    stack.popleft()
                else:
                    if stack[0] == float('inf'):
                        res.appendleft(0)
                    else:
                        res.appendleft(stack[0])
                    stack.appendleft(rev.val)
                    break
            
            rev = rev.next
        return res
'''
2 1 5



'''