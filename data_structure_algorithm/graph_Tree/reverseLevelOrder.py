from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None,None
def traverse(root):
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
   # result = result.reverse()
    return result[::-1]

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse Level order traversal: "+str(traverse(root)))
main()