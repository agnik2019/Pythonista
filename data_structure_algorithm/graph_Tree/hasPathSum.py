# Binary Tree Path Sum
class TreeNode:
    def __init__(self,val,left=None,right = None):
        self.val = val
        self.left, self.right = left,right

def hasPath(root, sum):
    if root is None:
        return False

    if root.val == sum and root.left is None and root.right is None:
        return True

    return hasPath(root.left , sum-root.val) or hasPath(root.right, sum-root.val)    
    
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(hasPath(root,23))
    print(hasPath(root,16))
  
main()