class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ispositive = (dividend<0) == (divisor<0)
        a,b,ans = abs(dividend),abs(divisor),0
        while a>=b:
            q = 0
            while a> (b<<(q+1)):
                q += 1
            ans += 1<<q
            a =a -(b<<q)
        return min(ans if ispositive else -ans, 2147483647)
        