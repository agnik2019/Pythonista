"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            previousNode = None
            levelsize = len(queue)
            for _ in range(levelsize):
                currentNode = queue.popleft()
                if previousNode:
                    previousNode.next = currentNode
                previousNode = currentNode
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        return root
        