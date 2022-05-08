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

def merge(l1,l2):
    dummy = listNode(-101)
    head = dummy
    while l1 and l2:
        if l1.value < l2.value:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next
        dummy = dummy.next
    if l1: dummy.next = l1
    if l2 : dummy.next = l2
    return head.next

def sortList(head):
    # if linkedlist has 0 or 1 node
    if head is None or head.next is None:
        return head
    slow, fast, temp = head,head,None
    
    while fast and fast.next:
        temp = slow
        slow = slow.next
        fast = fast.next.next
    
    temp.next = None
    head = sortList(head)
    slow = sortList(slow)
    return merge(head,slow)



def main():
    head = listNode(8)
    head.next = listNode(4)
    head.next.next = listNode(2)
    head.next.next.next = listNode(1)

    print("Nodes with original list nodes ")
    head.print_list()


    result = sortList(head)
    print("Nodes with sorted list nodes ")
    result.print_list()

main()
