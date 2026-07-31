# Implement Student, Faculty and PhdStudent classes here

class Student:
    def __init__(self,sid,deptid):
        self.sid=sid
        self.deptid = deptid
    def get_info(self):
        return f"StudentID:{sid} DepartmentID:{deptid}"
    
class Faculty:
    def __init__ (self,eid,deptid):
        self.deptid=deptid
        self.eid=eid 
    
    def get_info (self):
        return f"EmployeeID:{eid} DepartmentID:{deptid}" 

class PhDStudent(Student,Faculty):
    def __init__(self,sid,eid,deptid):
        Student.__init__(self,sid,deptid)
        Faculty.__init__(self,eid,deptid)
    def get_info(self):
        return f"StudentID:{sid} EmployeeID:{eid} DepartmentID:{deptid}"
        
        



