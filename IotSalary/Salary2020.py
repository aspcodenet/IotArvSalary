

from abc import ABC, abstractmethod
import datetime
#alla timanställda har 100 kr
# SALES monthlySalary grundlön- provision 2% av sålt för 



class Employee(ABC): # Däggdjur
    def __init__(self,namn, birthDate,accountNo):
        self._birthDate = birthDate
        self._accountNo = accountNo
        self._namn = namn

    @abstractmethod
    def CalculateSalary(self):
        return 0


    def CreateSalaryTransaction(self):
        return f"{self._namn},{self._accountNo},{self.CalculateSalary()}"

    #def __init__(self,namn, birthDate,accountNo, monthlySalary, hoursWorked, soldFor):
    #    self._birthDate = birthDate
    #    self._accountNo = accountNo
    #    self._namn = namn
    #    self._monthlySalary = monthlySalary
    #    self._hoursWorked = hoursWorked
    #    self._soldFor = soldFor

    #def CalculateSalary(self):
    #    if self._monthlySalary == 0:
    #        return self._hoursWorked * 100
    #    if self._soldFor > 0:
    #        return self._monthlySalary + (self._soldFor * 0.02)
    #    return self._monthlySalary

class MonthlyEmployee(Employee): #Motsvarande människa
    def __init__(self,namn, birthDate,accountNo,monthlySalary):
        super().__init__(namn, birthDate,accountNo)
        self._monthlySalary = monthlySalary

    def CalculateSalary(self):
        return self._monthlySalary

class HourlyEmployee(Employee): #Motsvarande människa
    def __init__(self,namn, birthDate,accountNo,hoursWorked):
        super().__init__(namn, birthDate,accountNo)
        self._hoursWorked = hoursWorked

    def CalculateSalary(self):
        return self._hoursWorked * 100


class SalesmanEmployee(MonthlyEmployee): #Motsvarande människa
    def __init__(self,namn, birthDate,accountNo,monhtlySalary, soldFor ):
        super().__init__(namn, birthDate,accountNo,monhtlySalary)
        self._soldFor = soldFor

    def CalculateSalary(self):
        return self._monthlySalary + (self._soldFor * 0.02)

rectangle.calculateArea()

p1 = MonthlyEmployee("Stefan", datetime.date(1972,8,3),"111-223454",5000)
p2 = MonthlyEmployee("Kerstin", datetime.date(1973,3,5),"111-1312132",6000)
p3 = HourlyEmployee("Josefine", datetime.date(2002,3,30),"111-33213",10)
p4 = SalesmanEmployee("Oliver", datetime.date(2008,5,28),"112-767765",3000,10000)
p5 = Employee("321321231",datetime.date(2008,5,28),"112-767765")
#Skapa ett Däggdjur. Manniska, Rat, Kangaroo


d = {}

d["stefan"] = p1
d["kerstin"] = MonthlyEmployee("Kerstin", datetime.date(1973,3,5),"111-1312132",6000)





allEmployees = []
allEmployees.append(p1)
allEmployees.append(p2)
allEmployees.append(p3)
allEmployees.append(p4)

for emp in allEmployees:
    print(emp.CreateSalaryTransaction())

