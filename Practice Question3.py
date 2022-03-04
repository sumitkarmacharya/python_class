from unicodedata import name


class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print(self.name)
        print(self.roll)
    def setAge(self,age):
        self.age=age
        return age
    def setMarks(self,marks):
        self.marks=marks
        return marks
student=Student("Sumit",5)
student.display()
print(student.setAge(24))
print(student.setMarks(72))

        