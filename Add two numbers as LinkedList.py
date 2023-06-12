class Solution:
    def addTwoNumbers(self, l1, l2):
        head = sm = ListNode()                           
        carry = 0                                         
        while l1 or l2:                                   
            if l1: carry, l1 = carry + l1.val, l1.next    
            if l2: carry, l2 = carry + l2.val, l2.next    
            sm.next = sm = ListNode(val = carry % 10)     
            carry //= 10                                 
        if carry: sm.next = ListNode(val = carry)        
        return head.next