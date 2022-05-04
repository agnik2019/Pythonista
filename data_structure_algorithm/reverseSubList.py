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

def reverse_sublist(head,p,q):
    if p == q:
        return head
    previous,current = None,head
    i = 0
    while current is not None and i<p-1:
        previous = current
        current = current.next
        i += 1

    last_node_of_first_part = previous
    last_node_of_sublist = current

    next = None
    i = 0
    while current is not None and i < q-p+1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1
    
    if last_node_of_first_part is not None:
        last_node_of_first_part.next = previous  
    else:
        head = previous

    last_node_of_sublist.next = current
    return head

def main():
    head = listNode(1)
    head.next = listNode(2)
    head.next.next = listNode(3)
    head.next.next.next = listNode(4)
    head.next.next.next.next = listNode(5)

    print("Nodes with original list nodes ")
    head.print_list()


    result = reverse_sublist(head,2,4)
    print("Nodes with reversed list nodes ")
    result.print_list()

main()
