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
    def mirror(self,root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1.val != root2.val:
            return False
        return self.mirror(root1.left,root2.right) and self.mirror(root1.right, root2.left)
 
    
def main():
    sol = Solution()
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print(str(root1.traverse()))


    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)

    print(str(root2.traverse()))

    print(sol.mirror(root1,root2))


main()