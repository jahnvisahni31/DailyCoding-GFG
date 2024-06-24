#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # code here 
        if q > n*2:
            return 0
        count = 0
        k = 2 + (n-1)
        if k<q:
            ans = q - k
            i = ans + 2
        else:
            i =2
        aj = n+1
        if aj > q:
            ans1 = q
        else:
            ans1 = aj

        
        return(ans1 - i) +1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends