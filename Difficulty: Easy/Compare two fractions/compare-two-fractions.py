#User function Template for python3


class Solution:
    def compareFrac (self, str):
        
        # code here
        f1, f2 = str.split(', ')
        a, b = map(int, f1.split('/'))
        c, d = map(int, f2.split('/'))
        e = a / b
        f = c / d
        if e > f:
            return f1
        elif e < f:
            return f2
        else:
            return "equal"
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends