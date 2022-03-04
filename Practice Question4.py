class Time:
    def __init__(self,hours,minute):
        self.hours=hours
        self.minute=minute
    def addtime(self,hour1,minute1,hour2,minute2):
        Total_time=hour1*60+minute1+hour2*60+minute2
        print(Total_time//60,"hour",Total_time%60,"minute")
    def displayTime(self):
        print(self.hours,"hours",end=" ")
        print(self.minute,"minutes")
    def DisplayMinute(self):
        return self.hours*60+self.minute
time=Time(2,45)
time.addtime(1,20,1,30)
time.displayTime()
print(time.DisplayMinute())