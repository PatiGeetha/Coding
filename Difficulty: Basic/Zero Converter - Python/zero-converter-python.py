def pos(n):
    if n==0:
        print("already ZERO")
    if (n>0):
        print(*range(n-1,-1,-1),end=" ")
    
def neg(n):
    if (n<0):
        print(*range(n,1,1), end=" ")

