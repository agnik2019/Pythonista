from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None,None

def minDepthOfTree(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    minimumDepth = 0
    while queue:
        minimumDepth += 1
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # check if this is a leaf node
            if not currentNode.left and not currentNode.right:
                return minimumDepth
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(11)
    print("Minimum depth of the tree: "+str(minDepthOfTree(root)))
main()