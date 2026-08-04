class Solution:
    def gcd(self, a, b):
        while(a!=0 and b!=0):
            if a>b:
                a = a%b
            else:
                b = b%a
        if(a==0): return b
        if(b == 0): return a
            

        