class Temperature:
    def __init__(self,unit):
        self.unit=unit
    def convertFahrenheit(self):
        return self.unit*1.8+32
    def convertCelcius(self):
        return ((self.unit-32)*5)/9
Unit=Temperature(24)
print("{:.2f}".format(Unit.convertFahrenheit()))         