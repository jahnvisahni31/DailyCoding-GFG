#User function Template for python3

class Solution:
    def makeEven(self, s):
        # code here
        s = list(s)
        for i in range(len(s)):
            if (int(s[i])<int(s[-1])) and (int(s[i])%2==0):
                s[i],s[-1]=s[-1],s[i]
                return "".join(s)
                
        for i in range(1,len(s)+1):
            if (int(s[-i])>int(s[-1])) and (int(s[-i])%2==0):
                s[-i],s[-1]=s[-1],s[-i]
                return "".join(s)
                
        return "".join(s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        Str = input()
        ob = Solution()
        print(ob.makeEven(Str))


# } Driver Code Ends