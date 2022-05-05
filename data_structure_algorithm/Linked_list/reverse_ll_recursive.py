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

def recursive_reverse(curr,prev):
    if curr == None:
        return prev
    newNode = curr.next
    curr.next = prev
    return recursive_reverse(newNode,curr)

def reverse(head):
    # write your code here
    return recursive_reverse(head,None)

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
