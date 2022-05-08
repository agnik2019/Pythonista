class MinStack(object):

    def __init__(self):
        self.a , self.b = [],[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.a.append(val)
        if (len(self.b) == 0):
            self.b.append(val)
        else:
            minelement = min(val,self.b[-1])
            self.b.append(minelement)
        

    def pop(self):
        """
        :rtype: None
        """
        self.a.pop()
        self.b.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.a[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.b[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()