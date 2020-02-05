class consultant:
    def __init__(self,nam="",exp=0,skl="",sal=0):
        self.__name=nam;self.__experiance=exp;self.__skill=skl;self.__pay=sal
    def __str__(self):
        return self.__name+" "+str(self.__experiance)+" "+self.__skill+" "+str(self.__pay)
    def setName(self,nam):
        self.__name=nam
    def getName(self):
        return self.__name
    def setExperiance(self,exp):
        self.__experiance=exp
    def getExperiance(self):
        return self.__experiance
    def setSkill(self,skl):
        self.__skill=skl
    def getSkill(self):
        return self.__skill

    def setPay(self, sal):
        if self.__experiance>=5 or self.__experiance<=10 and self.__skill=="java" or self.__skill=="python" :
            sal = 12000
            self.__pay=sal
        elif self.__experiance>=3 or self.__experiance<=8 and self.__skill=="ai" or self.__skill=="python" :
            sal = 7000
            self.__pay=sal
        elif self.__experiance>=4 or self.__experiance<=10 and self.__skill=="java" or self.__skill=="c" or self.__skill=="c++":
            sal = 5000
            self.__pay=sal

    def getPay(self):
        return self.__pay
c1=consultant()
c2=consultant()
c3=consultant()
c4=consultant()
c1.setName("Veena");c1.setExperiance(7);c1.setSkill("python");c1.setPay(0);
c2.setName("Megha");c2.setExperiance(5);c2.setSkill("ai");c2.setPay(0);
c3.setName("Samuel");c3.setExperiance(9);c3.setSkill("java");c3.setPay(0);
c4.setName("Skanda");c4.setExperiance(7);c4.setSkill("c");c4.setPay(0);
print(c1.getName(),c1.getExperiance(),c1.getSkill(),c1.getPay())
print(c2.getName(),c2.getExperiance(),c2.getSkill(),c2.getPay())
print(c3.getName(),c3.getExperiance(),c3.getSkill(),c3.getPay())
print(c4.getName(),c4.getExperiance(),c4.getSkill(),c4.getPay())

