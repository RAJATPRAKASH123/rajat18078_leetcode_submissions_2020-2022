// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        def reverseFun(head):
            if not head.next:
                return head
            newHead = reverseFun(head.next)
            head.next.next = head
            head.next = None
            return newHead

        return reverseFun(head)
        

'''

        1 ->    2 ->    3 ->    4 ->   5 ->   None
        cur
        ```` 
        (head) 
None <- 1  <-   2   <-  3 ....      <- 5(head)     
     ````

What do we want to achieve?

Ans?

  5 -> 4 -> 3 -> 2 -> 1 -> None
head




None <-  1  <-  2  <-   3   <-  4  <-  5    None
                                            future
                                            cur
                                    prev


GOAL --
None <- 1  <-   2   <-  3 ....      <- 5(head)  

cur = headsw
prev = None
future = None
while cur != None:
    future = cur.next
    cur.next = prev
    prev = cur
    cur = future
head = prev

Q) Why we are using future? When we can use the cur.next to access next element?
'''


'''



def printOneToN(1 ...  n):
    printOneToN(1 ... n-1)
    print(n)

def reverseFun(1 -> 2 -> 3 -> 4 -> 5 -> None): None <- 1 <- 2 <- 3 <- 4 <- 5
               h                                                         

    sub = reverseFun(2 -> 3 -> 4 -> 5) :: None <- 2 <- 3 <- 4 <- 5
                                                                 
    
def reverseFun(head):
    reverseFun(head.next)
                        None <- 2 <- 3 <- 4 <- 5

                        1 -> 2
                        h,   h.next

                        None      <- 2 <- 3 <- 4 <- 5
                        h.next.next     h.next
    
    head.next.next = head
    
    1 -> 2
    1 <- 2 <- 3 <- 4 <- 5

    head.next = None
    None <- 1 <- 2 <- 3 <- 4 <- 5

def reverseFun(head):
    if not head.next:
        head.next 
        return head
    newHead = reverseFun(head.next)
    head.next.next = head
    head.next = None
    return newHead

Initially :

1 -> 2 -> 3 -> None
h

Executed Step : reverseFun(head.next)

1 -> 2 
h

None <- 2 <- 3

Executed Step : head.next.next = head

1 -> 2
1 <- 2 <- 3

Executed Step : head.next = None

None <- 1 <- 2 <- 3
        h






'''