from threading import*
from array import *
class employ(Thread):
    def __init__(self,name=""):
        Thread.__init__(self);self.name=name
    ctc = ['f',4.5, 9.2, 12.3, 2.8, 9.1, 4.5, 6.2]
    def salary(self):
        freeze.acquire()
        max=float(input("Enter the maximum salary"))
        min=float(input("Enter the minimum salary"))
        for check in self.ctc:
            sd=self.ctc[check]
            if max<=sd and min>=sd:
                sd=sd+10/100
                if sd > 9.0 and sd <= 13.0:
                    print("Sorry,u r Fired", sd)
                elif sd <= 9.0 and sd >= 4.5:
                    print("Promoted as Team Leader", sd)
                elif sd >= 4.5 and sd <= 3.0:
                    print("Onsite oppurtunity", sd)
                else:
                    print("You are  same as you are", sd)

        freeze.acquire()


    def run(self):
        self.salary()
freeze=Lock()


s1=employ();s1.start()
s2=employ();s2.start();
