class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1: return "1"
        fact = [1]*10
        for i in range(1,10):
            fact[i] = i*fact[i-1]
        digits = []
        for i in range(1,n+1):
            digits.append(i)
        ans = ""
        def recur(n,k):
            nonlocal ans
            if n == 1:
                ans += str(digits[-1])
                return
            idx = k//fact[n-1]
            if k%fact[n-1] == 0:
                idx -= 1
            ans += str(digits[idx])
            digits.pop(idx)
            k -= fact[n-1]*idx
            recur(n-1,k)
        recur(n,k)
        return ans