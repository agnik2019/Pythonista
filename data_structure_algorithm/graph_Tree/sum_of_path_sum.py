# Binary Tree Path Sum
class TreeNode:
    def __init__(self,val,left=None,right = None):
        self.val = val
        self.left, self.right = left,right

def SumPath(currentNode,pathSum):
    if currentNode is None:
        return 0
    pathSum = 10 * pathSum + currentNode.val
    if currentNode.left is None and currentNode.right is None:
        return pathSum

    return SumPath(currentNode.left ,pathSum) + SumPath(currentNode.right, pathSum)    
    
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(SumPath(root,0))
  
main()