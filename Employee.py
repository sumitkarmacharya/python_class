class Employee:
    def __init__(self,name,salary,taxpercent):
        self.name=name
        self.salary=salary
        self.taxpercent =taxpercent
    def netsalary(self):
        salaryaftertax= self.salary-self.salary*self.taxpercent
        return salaryaftertax
Employee1 = Employee("Sumit",25000,0.01)
Employee2 = Employee("Suman",26000,0.01)
Employee3 = Employee("Himal",27000,0.01)
print(Employee1.netsalary())


