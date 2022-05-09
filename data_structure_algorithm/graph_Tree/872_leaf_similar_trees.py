# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def dfs(self,root,res):
        if root is None:
            return []
        if not root.left and not root.right:
            res.append(root.val)
        if root.left:
            self.dfs(root.left,res)
        if root.right:
            self.dfs(root.right,res)
        return res

            
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf1 = []
        self.dfs(root1,leaf1)
        print(leaf1)
        leaf2 = []
        self.dfs(root2,leaf2)
        print(leaf2)
        return leaf1 == leaf2
    
def main():
    sol = Solution()
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)

    print(sol.leafSimilar(root1,root2))

main()