
from collections import Counter
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        res=0
        d=Counter(s)
    
        for i in d:
            if d[i]%2==ord(i)%2:
                res+=1
        if res%2==0:
            return "EVEN"
        return "ODD"
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends