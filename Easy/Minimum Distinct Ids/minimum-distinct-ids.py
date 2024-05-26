#User function Template for python3
from collections import Counter
class Solution:
    def distinctIds(self,arr : list, n : int, m : int):
        # Complete this function
        count = Counter(arr)
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        while count and count[-1][1] <= m:
            m -= count.pop()[1]
        return len(count)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        m = int(input())
        ob=Solution()
        print(ob.distinctIds(arr, n, m))
# } Driver Code Ends