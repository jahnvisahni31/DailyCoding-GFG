#User function Template for python3

import datetime
class Solution:
    def getDayOfWeek(self, d, m, y):
        # code here 
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
        date = datetime.date(y, m, d)
        day_index = date.weekday()
    
        return days_of_week[day_index]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        d,m,y=map(int,input().split())
        
        ob = Solution()
        print(ob.getDayOfWeek(d,m,y))
# } Driver Code Ends