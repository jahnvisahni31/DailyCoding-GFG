#User function Template for python3

class Solution:
    def countNumbers(self, n):
        # code here
        count = 0 
        for i in range(1, n+1):
            while i:
                lastdigit = i%10 
                if lastdigit<1 or lastdigit>5:
                    break 
                i //= 10 
                
            else:
                count+=1 
                    
        return count 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.countNumbers(n)
        print(ans)
        tc -= 1

# } Driver Code Ends