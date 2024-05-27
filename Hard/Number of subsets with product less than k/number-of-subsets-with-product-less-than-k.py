#User function Template for python3

class Solution:
    def numOfSubsets(self, arr, N, K):
        # code here 
        def rec(i,p):
            nonlocal K,N
            if(p in dp[i]):
                return dp[i][p]
            dp[i][p]=0
            for j in range(i,N):
                if(p*arr[j]<=K):
                    dp[i][p]+=1+rec(j+1,p*arr[j])
            return dp[i][p]
        dp=[{} for i in range(N+1)]
        return rec(0,1)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        K=int(input())
        
        ob = Solution()
        print(ob.numOfSubsets(arr,N,K))
# } Driver Code Ends