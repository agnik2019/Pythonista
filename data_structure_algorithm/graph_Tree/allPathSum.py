# Binary Tree Path Sum
class TreeNode:
    def __init__(self,val,left=None,right = None):
        self.val = val
        self.left, self.right = left,right
def findPath(root,sum):
    allPaths = []
    findPathRecursive(root, sum,[], allPaths)
    return allPaths

def findPathRecursive(currentNode, sum, currentPath, allPaths):
    if currentNode is None:
        return 

    # choose
    currentPath.append(currentNode.val)
    # explore
    if currentNode.val == sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath))
    else:
        findPathRecursive(currentNode.left , sum-currentNode.val,currentPath,allPaths) 
        findPathRecursive(currentNode.right, sum-currentNode.val,currentPath,allPaths) 
    # unchoose
    del currentPath[:1]
    
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(findPath(root,23))
    print(findPath(root,16))
  
main()