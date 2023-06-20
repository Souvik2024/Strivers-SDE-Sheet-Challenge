class Solution:
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
        length = 1
        curr = head
        while curr.next is not None:
            length += 1
            curr = curr.next
        curr.next = head
        k %= length
        lengthPrev = length - k - 1
        curr = head
        for _ in range(lengthPrev):
            curr = curr.next
        res = curr.next
        curr.next = None
        return res