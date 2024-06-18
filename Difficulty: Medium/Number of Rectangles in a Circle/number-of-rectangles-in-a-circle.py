#User function template for Python

class Solution:
    def rectanglesInCircle(self,r):
        #code here
        ans = 0
        limit = 2 * r * 2 * r
        for i in range(1, 2 * r + 1):
            for j in range(1, 2 * r + 1):
                if i * i + j * j <= limit:
                    ans += 1
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)

# } Driver Code Ends