
class Node:
	def __init__(self, d):
		self.data = d
		self.left = None
		self.right = None

def sortedArrayToBST(arr):	
	if not arr:
		return None
	mid = (len(arr)) // 2
	
	root = Node(arr[mid])
	root.left = sortedArrayToBST(arr[:mid])

	root.right = sortedArrayToBST(arr[mid+1:])
	return root

def printAncestors(root, target):    
    if root == None:
        return False
    if root.data == target:
        print(root.data)
        return True

    if (printAncestors(root.left, target) or
        printAncestors(root.right, target)):
        print(root.data,end=' ')
        return True
 
    return False


def preOrder(node):
	if not node:
		return
	
	print(node.data)
	preOrder(node.left)
	preOrder(node.right)

#arr = [8,6,5,9,47,84]
strarr = "84798456"
arr = []
flag = 0
onedigit,twodigit = 0,0
i = 0
while i<len(strarr):
    if flag== 0:
        onedigit = int(strarr[i])
        arr.append(onedigit)
        i += 1
        flag = 1
    else:
        twodigit = int(strarr[i:i+2])
        arr.append(twodigit)
        i += 2
        flag = 0
    #print(f"{onedigit}  {twodigit}")
print(arr)
arr.sort(reverse=True)
root = sortedArrayToBST(arr)
print("PreOrder Traversal of constructed BST ")
preOrder(root)
print("ancestor")
printAncestors(root, 84)
