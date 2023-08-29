from company import *

empdata = dict()
# collection of Employee data

class Employee(Company):
    
    def __init__(self,companyid,companyname,empid,empname,empdept,emprole,empsal,emphrs):
        # inheitence and parameterized constructor of employee class
        super().__init__(companyid,companyname)
        self.empid = empid
        self.empname=empname
        self.empdept = empdept
        self.emprole=emprole
        self.empsal=empsal
        self.emphrs=emphrs
        empdata[self.empid] = [self.companyid,self.companyname,self.empname,self.empdept,self.emprole,self.empsal,self.emphrs]
        
    def displayEmployees(self):
        # implements display functionality
        print(self.companyname," ",self.empname," ",self.empid," ",self.empdept," ",self.emprole)
    
    def searchEmployee(self,eid,empdept,emprole):
        # implements search functionality
        if empdata[eid] and empdata[eid][3]==empdept and empdata[eid][4]==emprole:

            titles = ['Company ID: ','Company Name: ','Employee Name: ','Employee Dept: ','Employee Role: ']
            print("Search Results: ")
            for i in range(len(empdata[eid])-2):
                 
                 print(titles[i],empdata[eid][i],end=" ")
            print("")

            
                 
                 
        else:
            print ("No Employee with details ",eid," ",empdept," ",emprole)
    

    def getEmpData(self):
            # return employee data
            return empdata
  
    def calculateSalary(self,empid):
         if empdata[empid]:
              print("Salary of ",empdata[empid][2]," is ",empdata[empid][5]*empdata[empid][6])
         else:
              
              print("Employee not found")

     





