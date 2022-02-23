class Employee:
    def __init__(self,name,salary,tax_percent):
        self.name = name
        self.salary = salary
        self.tax_percent = tax_percent
    def net_salary(self):
        salary_after_tax = self.salary-self.salary*self.tax_percent
        return salary_after_tax
Employee1 = Employee("Sumit",25000,0.01)
Employee2 = Employee("Suman",26000,0.01)
Employee3 = Employee("Hemant",26000,0.01)
print(Employee2.name)
print(Employee2.salary)
print(Employee2.net_salary())
print(int(Employee2.tax_percent*100),"%")