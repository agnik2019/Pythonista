# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # This function creates a parent map
    def createparentmap(self,root,parent,parent_map):
        if root is None:
            return
        parent_map[root] = parent
        self.createparentmap(root.left,root,parent_map)
        self.createparentmap(root.right,root,parent_map)
        
    # actual main functiom
    def helper(self,root,k,parent_map,visited,res):
        if root == None or visited.count(root)>0 or k < 0:
            return
        visited.append(root)
        if k == 0:
            res.append(root.val)
            return
        self.helper(root.left,k-1,parent_map,visited,res)
        self.helper(root.right,k-1,parent_map,visited,res)
        self.helper(parent_map[root],k-1,parent_map,visited,res)
        
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        res = []
        parent_map = {}
        visited = []
        parent = None
        self.createparentmap(root,parent,parent_map)
        self.helper(target,k,parent_map,visited,res)
        return res