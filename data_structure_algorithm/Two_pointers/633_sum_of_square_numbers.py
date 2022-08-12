import math

# Brute force solution
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range (0,int(math.sqrt(c))+1):
            for j in range(0,int(math.sqrt(c))+1):
                if c == i*i + j*j:
                    return True
        return False

print(Solution().judgeSquareSum(5))

# Optimized using b = sqrt(a*a - c)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range (0,int(math.sqrt(c))+1):
            j = math.sqrt(c - i*i)
            if j == int(j):
                return True
        return False