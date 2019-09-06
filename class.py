from datetime import date
class student:
    passing_per = 45
    
    def __init__(self, name, age=25, percentage=85):
        self.name = name
        self.age = age
        self.percentage = percentage
        
    @classmethod
    def fromtheyear(cls,name,year,percentage):
        return cls(name, date.today().year - year, percentage)
    
    def studentdetail(self):
        
        print('name = ', self.name)
        print('age =', self.age)
        
        print('per = ', self.percentage)
    def ispass(self):
        if self.percentage > student.passing_per:
            print('pass')
        else:
           print('fail')
    @staticmethod
    def welcome():
        print('hey! welcome')
s1 = student('satyam')
s1 = student.fromtheyear('satyam',1997,80)
s1.studentdetail()



            