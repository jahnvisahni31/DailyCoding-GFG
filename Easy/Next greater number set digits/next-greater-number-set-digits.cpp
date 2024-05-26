//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution
{
    public:
    int findNext (int N) 
    {
        //code here.
        string s = to_string(N);
        bool b = next_permutation(s.begin(),s.end());
        if(!b) return -1;
        return stoi(s);
    }  
};

//{ Driver Code Starts.
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n; cin >> n;
		Solution ob;
		int res = ob.findNext (n);
		if (res == -1)
		    cout << "not possible";
		else
		    cout << res;
		cout << endl; 
	}
}
// } Driver Code Ends