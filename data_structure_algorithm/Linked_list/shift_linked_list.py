# 1 -> 2 -> 3 -> 4 -> 5               k = 3
# 3 -> 4 -> 5 -> 1 -> 2

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

def shift_LL(head,k):
    listLength = 1
    listTail = head
    while listTail.next is not None:
        listTail = listTail.next
        listLength += 1


    offset = abs(k) % listLength

    if offset == 0:
        return head

    newTailPosition = listLength - offset if k>0 else offset

    newTail = head
    for i in range(1, newTailPosition):
        newTail = newTail.next
    
    newHead = newTail.next
    newTail.next = None
    listTail.next = head

    return newHead


def main():
    head = listNode(1)
    head.next = listNode(2)
    head.next.next = listNode(3)
    head.next.next.next = listNode(4)
    head.next.next.next.next = listNode(5)

    print("Nodes with original list nodes ")
    head.print_list()


    result = shift_LL(head,2)
    print("Nodes with reversed list nodes ")
    result.print_list()

main()