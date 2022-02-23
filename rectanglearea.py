from unicodedata import name


class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
rectangle1=rectangle(26,32)
rectangle2=rectangle(42,32)
print(rectangle2.area())