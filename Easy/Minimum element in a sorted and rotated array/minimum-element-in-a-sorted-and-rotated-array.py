#User function Template for python3

class Solution:
    def findMin(self, arr, n):
        #complete the function here
        low = 0
        high = n - 1

        while low <= high:
            if arr[low] <= arr[high]:
                return arr[low]

            mid = low + (high - low) // 2

            prev = (mid - 1 + n) % n
            next = (mid + 1) % n

            if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
                return arr[mid]
            elif arr[mid] <= arr[high]:
                high = mid - 1
            else:
                low = mid + 1

        return -1 
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends