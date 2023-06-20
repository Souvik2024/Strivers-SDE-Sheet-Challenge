class Solution:
    def reverseKGroup(self, head, k):
        curr = temp = head
        nxt = None
        prev = None
        count = 0
        while temp and count<k:
            temp = temp.next
            count += 1
        if count < k: 
            return curr
        count = 0
        while curr and count<k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1
        if nxt :
            head.next = self.reverseKGroup(nxt, k)
        return prev