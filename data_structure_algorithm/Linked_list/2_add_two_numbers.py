class listNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.val,end=" ")
            temp = temp.next
        print()

def addTwoNumbers(l1, l2):

    dummy= head = listNode(-1)

    if l1 is None:
        return l2
    if l2 is None:
        return l1
    carry = 0
    while (l1 or l2):
        firstval = l1.val if l1 is not None else 0
        secondval = l2.val if l2 is not None else 0
        total = firstval + secondval + carry
        carry = total // 10
        total = total % 10
        newNode = listNode(total)
        dummy.next = newNode
        dummy = dummy.next
        
        l1 = l1.next if l1 is not None else l1
        l2 = l2.next if l2 is not None else l2
    
    if carry>0:
        dummy.next = listNode(1)
        
    return head.next

def main():
    head = listNode(2)
    head.next = listNode(4)
    head.next.next = listNode(3)

    head2 = listNode(5)
    head2.next = listNode(6)
    head2.next.next = listNode(4)

    print("1st linked list ")
    head.print_list()

    print("2nd linked list ")
    head2.print_list()


    result = addTwoNumbers(head,head2)
    print("addition of two list")
    result.print_list()

main()
