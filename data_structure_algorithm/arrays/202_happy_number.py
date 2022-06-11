class Solution(object):
    def find_square(self,num):
        summ = 0
        while num>0:
            digit = num % 10
            summ += digit*digit
            num = num // 10
        return summ
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow, fast = n,n
        while True:
            slow = self.find_square(slow)
            fast = self.find_square(self.find_square(fast))
            if slow == fast:
                break
        return slow == 1

sol = Solution()
print(sol.isHappy(23))
        