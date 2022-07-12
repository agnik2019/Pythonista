# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:return False
        def calculate(root,x,y):
            if root.val == 2:
                return x or y
            elif root.val == 3:
                return x and y
        if not root.left and not root.right:
            return True if root.val == 1 else False
        x = self.evaluateTree(root.left)
        y = self.evaluateTree(root.right)
        return calculate(root,x,y)