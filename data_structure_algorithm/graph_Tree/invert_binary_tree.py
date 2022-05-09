from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def traverse(self):
        root = self
        result = []
        if root is None:
            return result
        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize):
                currentNode = queue.popleft()
                currentLevel.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            result.append(currentLevel)
        return result

class Solution(object):
    def invertTree(self,node):
        if node is None:
            return 
        node.left, node.right = node.right, node.left
        self.invertTree(node.left)
        self.invertTree(node.right)
    
def main():
    sol = Solution()
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print(str(root1.traverse()))
    sol.invertTree(root1)
    print(str(root1.traverse()))

    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)

    print(str(root2.traverse()))
    sol.invertTree(root2)
    print(str(root2.traverse()))

main()