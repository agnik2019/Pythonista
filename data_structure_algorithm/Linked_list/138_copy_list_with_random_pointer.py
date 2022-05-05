# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        ptr = head
        mp = {}
        while ptr:
            mp[ptr] = Node(ptr.val,None,None)
            ptr = ptr.next
        
        ptr = head
        while ptr:
            if ptr.next :
                mp[ptr].next = mp[ptr.next]
            if ptr.random:
                mp[ptr].random = mp[ptr.random]
            ptr = ptr.next
        
        return mp[head]
        



