class Solution(object):
    def removeNthFromEnd(self, head, n):
        pt1 = head
        pt2 = head
        for i in range(n):
            pt2 = pt2.next
        if pt2:
            while pt2.next is not None:
                pt1 = pt1.next
                pt2 = pt2.next
            pt1.next = pt1.next.next if pt1.next else None
        else:
            head = pt1.next
        return head