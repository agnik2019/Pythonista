# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy = ListNode(-101)
        head = dummy
        while list1 and list2:
            if list1.val < list2.val:
                newNode = ListNode(list1.val)
                dummy.next = newNode
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                dummy.next = newNode
                list2 = list2.next
            
            dummy = dummy.next
        
        if list1 :
            dummy.next = list1
        if list2:
            dummy.next = list2
        
        return head.next