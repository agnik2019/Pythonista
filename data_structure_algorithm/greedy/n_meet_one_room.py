#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
       # code here
       meet=[]
       for i in range(n):
           meet.append([end[i],start[i],i+1])
       meet.sort()
       endTime=meet[0][0]
       count=1
       for i in range(1,n):
           if meet[i][1]>endTime:
               endTime=meet[i][0]
               count+=1
       return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends