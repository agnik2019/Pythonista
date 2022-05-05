# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reversell(self,l1):
        previous, current, next = None,l1,None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = head = ListNode(-1)
        l1 = self.reversell(l1)
        l2 = self.reversell(l2)
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carry = 0
        while l1 or l2 :
            firstVal = l1.val if l1 else 0
            secondVal = l2.val if l2 else 0
            total = firstVal+secondVal+carry
            
            carry = total // 10
            total = total % 10
            
            dummy.next = ListNode(total)
            dummy = dummy.next
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            
        if carry:
            dummy.next = ListNode(1)
        
        return self.reversell(head.next)
            
        