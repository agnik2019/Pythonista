from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None,None
def BottomView(root):
    result = []
    if root is None:
        return result
    mp = {}
    queue = deque()
    queue.append((root,0))
    while queue:     
        currentNode,hd = queue.popleft()
        mp[hd] = currentNode.val
        if currentNode.left:
            queue.append((currentNode.left,hd-1))
        if currentNode.right:
            queue.append((currentNode.right,hd+1))
    mp = sorted(mp.items())
    for _,v in mp:
        result.append(v)
    return result

def main():
    root = TreeNode(2)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(15)
    root.left.left.left= TreeNode(18)
    print("Bottom view of the binary tree: "+str(BottomView(root)))
main()