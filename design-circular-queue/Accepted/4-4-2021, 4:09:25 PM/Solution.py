// https://leetcode.com/problems/design-circular-queue



class MyCircularQueue:
    
    class qNode:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self, k: int):
        self.max_size = k
        self.qlen = 0

    def enQueue(self, value: int) -> bool:
        if self.qlen == 0:
            self.head = self.qNode(value) 
            # print(self.head.val)
            self.head.next = self.head
            self.last = self.head
            self.qlen += 1
            return True
        if self.qlen < self.max_size:
            cur = self.qNode(value)
            self.last.next = cur
            cur.next = self.head
            self.head = cur
            self.qlen += 1
            return True
        return False
            
            
    def deQueue(self) -> bool:
        if self.qlen == 0:
            return False
        if self.qlen == 1:
            self.head = None
            self.last = None
            self.qlen -= 1
            return True
        cur = self.head
        while cur.next != self.last:
            cur = cur.next
        cur.next = self.head
        self.last = cur
        self.qlen -= 1
        return True

    def Front(self) -> int:
        if self.qlen == 0:
            return -1
        return self.last.val

    def Rear(self) -> int:
        if self.qlen == 0:
            return -1
        return self.head.val

    def isEmpty(self) -> bool:
        if self.qlen == 0:
            return True
        return False

    def isFull(self) -> bool:
        return self.qlen == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()