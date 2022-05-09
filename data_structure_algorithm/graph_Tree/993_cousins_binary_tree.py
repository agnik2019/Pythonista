# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def dfs(self,root,x,y,level,parent,levels,parents):
        if root is None:
            return
        if root.val == x:
            parents[0] = parent
            levels[0] = level
        if root.val == y:
            parents[1] = parent
            levels[1] = level
        
        self.dfs(root.left,x,y, level+1,root, levels,parents)
        self.dfs(root.right,x,y, level+1,root, levels,parents)
            
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        parents = [-1,-1]
        levels = [-1,-1]
        parent = TreeNode(-101)
        level = 0
        self.dfs(root,x,y,level,parent,levels,parents)
        # cousin -> save level and different parent
        if levels[0] == levels[1] and parents[0] != parents[1]:
            return True
        else:
            return False
        
    