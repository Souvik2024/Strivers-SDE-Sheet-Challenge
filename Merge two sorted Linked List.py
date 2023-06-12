class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        dummy_node = head
        while list1 and list2:
            if list1.val < list2.val:
                head.next = ListNode(list1.val)
                head = head.next
                list1 = list1.next
            else:
                head.next = ListNode(list2.val)
                head = head.next
                list2 = list2.next     
        if list1:
            head.next = list1
        if list2:
            head.next = list2  
        return dummy_node.next