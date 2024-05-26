#User function Template for python3

class Solution:
    def maxSum(self, n): 
        # code here 
        if n <= 4:
            return n
        p1 = self.maxSum(n//2)
        p2 = self.maxSum(n//3)
        p3 = self.maxSum(n//4)
        return max(n, p1+p2+p3)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))
# } Driver Code Ends