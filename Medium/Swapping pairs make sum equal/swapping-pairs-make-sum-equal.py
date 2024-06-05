class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        sum_a = sum(a)
        sum_b = sum(b)
        diff = sum_a - sum_b
        if diff % 2 != 0:
            return -1

        diff //= 2
        set_a = set(a)

        for num in b:
            if num + diff in set_a:
                return 1

        return -1

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends