# Implement the Person class
# code here
class Person():
        def __init__(self,name="Geeks",age=10):
            self.name=name
            self.age=age
        def set_name(self,name):
            self.name=name
        def set_age(self,age):
            self.age=age
        def get_name(self):
            return self.name
        def get_age(self):
            return self.age
obj=Person()
#obj.get_name()
#obj.get_age()
obj.set_name("jhon")
obj.set_age(21)

