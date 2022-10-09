class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        mp = {}
        cpx,cnt = 0,0
        for num in A:
            cpx = cpx ^ num
            if cpx == B:
                cnt += 1
            if cpx ^ B in mp:
                cnt += mp[cpx ^ B]
            mp[cpx] = mp.get(cpx,0)+1
        return cnt
