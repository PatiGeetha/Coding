class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        L1,T2=a,b
        while b>0:
            r=a%b
            a=b
            b=r
        gcd=a
        lcm=int((L1*T2)/gcd)
        return lcm,gcd