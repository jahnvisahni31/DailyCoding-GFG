#User function Template for python3

class Solution:
	def nthPoint(self,n):
		# Code here
		prev_term, current_term = 0, 1

        # Iterate through the sequence to find the nth term
        for i in range(1, n + 1):
            # Update terms using the Fibonacci recurrence relation
            prev_term, current_term = current_term, (prev_term + current_term) % (10**9 + 7)

        # Return the calculated nth term
        return current_term


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
# } Driver Code Ends