#User function Template for python3


# arr[] : the input array containing 0s and 1s
# N : size of the input array

# return the maximum length of the subarray
# with equal 0s and 1s
class Solution:
    def maxLen(self,arr, N):
        # code here
        max_length = 0
        count = 0
        dict = {0: -1}

        for i in range(len(arr)):
            if arr[i] == 0:
                count += 1
            else:
                count -= 1

            if count in dict:
                max_length = max(max_length, i - dict[count])
            else:
                dict[count] = i

        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().maxLen(a, len(a))
    print(s)
# } Driver Code Ends