#User function Template for python3

class Solution:
    
    def matrixMultiplication(self, N, arr):
        # code here
        dp = [[-1]*101 for _ in range(101)]
        def mcm(i,j):
            nonlocal dp
            if i>= j: return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = float("inf")
            for k in range(i,j):
                dp[i][j] = min(dp[i][j], mcm(i,k)+mcm(k+1,j)+arr[i-1]*arr[k]*arr[j])
                
            return dp[i][j]
        return mcm(1,N-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends