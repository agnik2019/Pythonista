class listNode:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next
        print()

def reorderList( head):
    """
    Do not return anything, modify head in-place instead.
    """
    def reverseLL(head):
        prev,cur,nxt = None,head,None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt 
        return prev
    # divide the list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    p,q = head,reverseLL(mid)
    dummy = p
    while  q:
       pp,qq = p,q
       p,q = p.next,q.next
       pp.next, qq.next = qq,p
    return dummy

def main():
    head = listNode(2)
    head.next = listNode(4)
    head.next.next = listNode(6)
    head.next.next.next = listNode(8)
    head.next.next.next.next = listNode(3)

    print("Nodes with original list nodes ")
    head.print_list()


    result = reorderList(head)
    print("Nodes with reversed list nodes ")
    result.print_list()

main()
