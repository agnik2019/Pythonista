# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.val,end=" ")
            temp = temp.next
        print()
class Solution(object):
    def length(self,head):
        len = 0
        while head:
            len += 1
            head = head.next
        return len
    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if self.length(head)<k :
            return head
        prev, curr, next = None,head,None
        for i in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head.next = self.reverseKGroup(curr,k)
        return prev


def main():
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(8)
    head.next.next.next.next = ListNode(10)

    print("Nodes with original list nodes ")
    head.print_list()


    sol = Solution()
    result = sol.reverseKGroup(head,2)
    print("Nodes with reversed list nodes ")
    result.print_list()

main()