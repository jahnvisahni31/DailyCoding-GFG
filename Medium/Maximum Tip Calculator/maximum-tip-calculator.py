
from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # code here
        tips = [(arr[i], brr[i]) for i in range(n)]
        tips.sort(key=lambda tip: abs(tip[0] - tip[1]), reverse=True)
    
        total_tip = 0
        for tipA, tipB in tips:
            if (x > 0 and tipA >= tipB) or y == 0:
                total_tip += tipA
                x -= 1
            else:
                total_tip += tipB
                y -= 1
    
        return total_tip


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

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends