class Solution:
    def minProd(self, arr):
        negatives = 0
        productOfAll = 1
        minNegativeNum = -11
        minPositiveNum = 11

        for i in arr:
            if i<0:
                negatives+=1
                minNegativeNum = max(minNegativeNum, i)
            else:
                minPositiveNum = min(minPositiveNum, i)
            if i!=0:
                productOfAll*=i

        if negatives == 0:
            return minPositiveNum
        elif negatives%2!=0:
            return productOfAll
        else:
            return productOfAll // minNegativeNum
