class Solution:
    def ExtractNumber(self,sentence):
        #code here
        nu = [wi for wi in sentence.split() if wi.isdigit() and '9' not in wi]
        if not nu:
            return -1
        nu = [int(num) for num in nu]
        la = max(nu)
        return la


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends