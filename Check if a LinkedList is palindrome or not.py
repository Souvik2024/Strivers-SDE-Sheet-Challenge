class Solution:
    def isPalindrome(self, head):
        ls = []
        while head != None:
            ls.append(head.val)
            head = head.next
        if ls == ls[::-1]:
            return True
        else: 
            return False