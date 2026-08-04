class Solution:
    def sumOfSeries(self,n):
        #code here
        res = n+1
        res = int((n*res)/2)
        return res**2
