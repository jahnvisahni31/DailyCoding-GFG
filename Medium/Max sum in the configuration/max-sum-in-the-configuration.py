#User function Template for python3

def max_sum(a,n):
    #code here
    totalSum = 0
    currentSum = 0
    for i in range(n):
        totalSum += a[i]
        currentSum += i * a[i]

    maxSum = currentSum
    for i in range(1, n):
        currentSum = currentSum + totalSum - n * a[n - i]
        maxSum = max(maxSum, currentSum)

    return maxSum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends