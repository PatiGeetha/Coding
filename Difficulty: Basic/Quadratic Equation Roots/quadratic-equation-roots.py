class Solution:
    def quadraticRoots(self, a, b, c):
        # code here
        D = b ** 2 - 4*a*c
        if D > 0:
            root1= math.floor( (-b+math.sqrt(D))/(2*a) )
            root2= math.floor((-b-math.sqrt(D))/(2*a))
            
        
        elif D == 0:
            root1 = math.floor(-b / (2*a))
            root2 = root1
            
        else:
            return [-1]
        
        if root1 > root2:
            return [root1,root2]
        else:
            return [root2,root1]
