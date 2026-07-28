class Solution:
    def utility(self, a, b, opr):
        if(opr==1):
            result=a+b
        elif(opr==2):
            result=a-b
        elif(opr==3):
            result=a*b
        else:
            result="Invalid Input"
            
        print(str(result))
        
        