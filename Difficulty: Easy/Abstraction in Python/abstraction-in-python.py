from abc import ABC, abstractmethod 
#  Implement both the classes here
class Shape(ABC):
    def __init__(self,color):
        self.color=color
    def get_color(self):
        return self.color
    @abstractmethod
    def get_area(self):
        pass
class Square(Shape):
    def __init__(self,c,side):
        super().__init__(c)
        self.side=side
    def get_area(self):
        self.side=side
        return self.side*self.side
