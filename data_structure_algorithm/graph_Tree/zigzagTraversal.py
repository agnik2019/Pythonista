from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None,None
def zigzagTraverse(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    leftToright = True

    while queue:
        levelSize = len(queue)
        currentLevel = deque()
        for _ in range(levelSize):
            currentNode = queue.popleft()
            if leftToright:
                currentLevel.append(currentNode.val)
            else:
                currentLevel.appendleft(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.append(list(currentLevel))
        leftToright = not leftToright
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Level order traversal: "+str(zigzagTraverse(root)))
main()