from employee import *

while(True):
    print(".......Welcome to Employee Management System.......")

    print("Enter 1 to add a COMPANY and EMPLOYEE details: ")
    print("Enter 2 to details of COMPANY and EMPLOYEE details: ")
    print("Enter 3 to search Employee Details: ")
    print("Enter 4 to calculate the Employee Salary: ")
    print("Enter * to EXIT: ")
    in1=input()
    if in1=='1':
        # case to handle insert operation on employee and company 
        ip1=int(input("Enter Company ID: "))
        inp2=input("Enter Company name: ")
        in3=int(input("Enter Employee ID: "))
        in4=input("Enter Employee Name: ")
        in10 = input("Enter Employee Dept: ")
        in5=input("Enter role of Employee: ")
        in6=int(input("Enter Employee Salary per hour: "))
        in7=int(input("Employee working hours: "))
        e1=Employee(ip1,inp2,in3,in4,in10,in5,in6,in7)
        print("Company and Employee added Successfully!!!")
    elif in1=='2':
        # case to handle Display Data of both company and employee
        print("........Displaying Employee Data...........")

        data = e1.getEmpData()
        titles = ['Company ID: ','Company Name: ','Employee Name: ','Employee Dept: ','Employee Role: ']
        for i in data:
            for j in range(len(data[i])-2):
                print(titles[j],data[i][j],end=" ")
        
        print("")

    elif in1=='3':
        # case to handle search functionality 
        eid=int(input("Enter Employee ID: "))
        ename = input('Enter Employee Dept: ')
        erole = input('Enter Employee Role: ')
        e1.searchEmployee(eid,ename,erole)
    
    elif in1=='4':
        empid = int(input('Enter Employee ID: '))

        e1.calculateSalary(empid)
    elif in1=='*':
        break;


    

