# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def SumPath(self,currentNode,pathSum):
        if currentNode is None:
            return 0
        pathSum = 2 * pathSum + currentNode.val
        if currentNode.left is None and currentNode.right is None:
            return pathSum

        return self.SumPath(currentNode.left ,pathSum) + self.SumPath(currentNode.right, pathSum)    
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.SumPath(root,0)
        