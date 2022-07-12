# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        def dfs(root,path,paths):
            path += str(root.val)
            if not root.left and not root.right:
                paths.append(path)
            if root.left: dfs(root.left,path+"->",paths)
            if root.right: dfs(root.right,path+"->",paths)
        if not root: return []
        else: dfs(root,"",paths)
        return paths