class Employee:
    def __init__(self,id,salary):
        self.id=id 
        self.salary = salary 
    def get_info(self):
        return f"EmployeeID:{id} Salary:{salary}" 
        
class SalesEmployee(Employee):
    def __init__(self,id,salary,sales=0):
        super().__init__(id,salary)  
    def get_info(self):
        return f"EmployeeID:{id} Salary:{salary} Sales:{sales}"

        