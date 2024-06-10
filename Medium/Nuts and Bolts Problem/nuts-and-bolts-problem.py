#User function Template for python3
class Solution:

	def matchPairs(self, n, nuts, bolts):
		# code here
		a = [ "!","#","$","%","&","*","?","@","^" ]
        i = 0
        for j in a:
            if j in nuts and bolts:
                k = nuts.index(j)
                v = bolts.index(j)
                nuts[i],nuts[k] = nuts[k],nuts[i]
                bolts[i],bolts[v] = bolts[v],bolts[i]
                i+=1
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(n, nuts, bolts)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends