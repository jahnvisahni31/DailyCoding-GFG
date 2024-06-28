#User function Template for python3

class Solution:
    def pattern (self, arr):
        # code here
        N = len(arr)
        def checkRowPalindrome(id_):
            l, r = 0, N - 1
            while l <= r:
                if arr[id_][l] != arr[id_][r]:
                    return False
                l += 1
                r -= 1
            return True
        def checkColPalindrome(id_):
            l, r = 0, N - 1
            while l <= r:
                if arr[l][id_] != arr[r][id_]:
                    return False
                l += 1
                r -= 1
            return True
        for i in range(N):
            if checkRowPalindrome(i):
                return str(i) + " R"
        for i in range(N):
            if checkColPalindrome(i):
                return str(i) + " C"
        return "-1"
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends