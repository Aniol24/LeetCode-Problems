class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        l3 = ListNode()
        pointer = l3

        while True:

            num = (l1.val + l2.val) + carry

            carry = num // 10

            pointer.next = ListNode(num % 10)
            pointer = pointer.next

            if l1.next == None and l2.next == None:
                break
            
            if l1.next == None:
                l1.next = ListNode()
            elif l2.next == None:
                l2.next = ListNode()

            l1 = l1.next
            l2 = l2.next  

        if carry >= 1:
            pointer.next =ListNode(carry)
            pointer = pointer.next 

        return l3.next   
        

l1 = ListNode(9, ListNode(4, ListNode(9)))
l2 = ListNode(9, ListNode(6, ListNode(9)))
addTwoNumbers = Solution().addTwoNumbers(l1, l2)
        