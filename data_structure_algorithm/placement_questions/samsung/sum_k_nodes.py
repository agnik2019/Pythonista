from collections import deque
class newNode :
    def __init__(self, val) :
        self.val = val
        self.left = None
        self.right = None

def sumOfNodesAtNthLevel(root,k):
    level = 0
    summ,flag = 0,0
    if root is None:
        return 0
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()

            if level == k:
                summ += currentNode.val
            else:
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        level += 1   
        # if flag == 1:
        #     break

        #result.append(currentLevel)
    return summ

# Driver code
if __name__ == "__main__" :
 
    # Tree Construction
    root = newNode(50)
    root.left = newNode(30)
    root.right = newNode(70)
    root.left.left = newNode(20)
    root.left.right = newNode(40)
    root.right.left = newNode(60)
    k = 2
    result = sumOfNodesAtNthLevel(root,k)
 
    # Printing the result
    print(result)