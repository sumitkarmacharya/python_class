class Circle:
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        return 3.14*self.radius**2
    def getCircumference(self):
        return 2*3.14*self.radius
circle=Circle(10)
print(circle.getArea())
print("{:.2f}".format(circle.getCircumference()))

