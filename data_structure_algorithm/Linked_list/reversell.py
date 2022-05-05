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

def reverse(head):
    # write your code here
    previous,current,next = None,head,None
    while(current is not None):
        next = current.next  # temporariy save the next pointer
        current.next = previous
        previous = current
        current = next

    return previous

def main():
    head = listNode(2)
    head.next = listNode(4)
    head.next.next = listNode(6)
    head.next.next.next = listNode(8)

    print("Nodes with original list nodes ")
    head.print_list()


    result = reverse(head)
    print("Nodes with reversed list nodes ")
    result.print_list()

main()
