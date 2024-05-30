
class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        # code here
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        
        # Initialize the first row with 1, as an empty string is a subsequence of any string
        for i in range(len(s1) + 1):
            dp[i][0] = 1
        
        # Loop through s1 and s2 and fill in the counts
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % int(1e9 + 7)
                else:
                    dp[i][j] = dp[i - 1][j] % int(1e9 + 7)
        
        return dp[len(s1)][len(s2)]
        

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s1 = (input())

        s2 = (input())

        obj = Solution()
        res = obj.countWays(s1, s2)

        print(res)

# } Driver Code Ends