
from typing import List


class Solution:
    def getPrimes(self, n : int) -> List[int]:
        # code here
        prime = [True for i in range(n+1)]
        prime[0] = prime[1] = False
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        for i in range(n):
            if prime[i] and prime[n-i]:
                return [i,n-i]
        return [-1,-1]


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends