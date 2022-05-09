from collections import deque
class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def maxDepth(root):
    """
    :type root: Node
    :rtype: int
    """
    if root is None:
        return 0
    queue = deque()
    queue.append(root)
    depth = 0
    while queue:
        levelsize = len(queue)
        for _ in range(levelsize):
            currentNode = queue.popleft()
            for child in currentNode.children:
                queue.append(child)
        depth += 1
    return depth


