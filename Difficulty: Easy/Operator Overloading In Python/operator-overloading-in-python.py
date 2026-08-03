class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    # Overload the + operator for adding two complex numbers
    def __add__(self, other):
        n=self.real+other.real
        n1=self.imaginary+other.imaginary
        return ComplexNumber(n,n1)
    
    # Overload the string representation of the object
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


        
        
