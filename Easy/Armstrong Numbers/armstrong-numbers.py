#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        digits = [int(i) for i in str(n)]
        s = sum(i ** 3 for i in digits)
        return "true" if s == n else "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends