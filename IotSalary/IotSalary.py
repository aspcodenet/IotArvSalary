from abc import ABC, abstractmethod
import datetime

#class Employee:
#    def __init__(self,birthDate,accountNo):
#        self._birthDate = birthDate
#        self._accountNo = accountNo
#        self._monthlySalary = 0
#        self._hoursWorked = 0
#        self._hourlySalary = 0
#        self._soldFor = 0


#    def SetSoldFor(self, soldFor):
#        self._soldFor = soldFor

#    def SetMonthlySalary(self, salary):
#        self._monthlySalary = salary

#    def SetHourlySalary(self, hourlySalary, hoursWorked):
#        self._hoursWorked = hoursWorked
#        self._hourlySalary = hourlySalary

#    def CreateSalaryTransaction(self):
#        salary = 0
#        if self._monthlySalary == 0:
#            salary = self._hoursWorked * self._hourlySalary
#        elif self._soldFor > 0:
#            salary = self._monthlySalary + self._soldFor * 0.02
#        else:
#            salary = self._monthlySalary

#        return f"{self._accountNo} {salary}"


class Employee(ABC):
    def __init__(self,namn, birthDate,accountNo):
        self._birthDate = birthDate
        self._accountNo = accountNo
        self._namn = namn

    @abstractmethod
    def CalculateSalary(self):
        return 0

    def CreateSalaryTransaction(self):
        return f"{self._namn} {self._accountNo} {self.CalculateSalary()}"


class MonthlyEmployee(Employee):
    def __init__(self,namn, birthDate,accountNo, monthlySalary):
        super().__init__(namn,birthDate,accountNo)
        self._monthlySalary = monthlySalary

    def CalculateSalary(self):
        return self._monthlySalary


class UnpaidMonthlySlave(MonthlyEmployee):
    def __init__(self,namn, birthDate,accountNo):
        super().__init__(namn,birthDate,accountNo, 0)

    def CalculateSalary(self):
        return 0


class HourlyEmployee(Employee):
    def __init__(self,namn, birthDate,accountNo, hoursWorked, hourlySalary):
        super().__init__(namn,birthDate,accountNo)
        self._hoursWorked = hoursWorked
        self._hourlySalary = hourlySalary

    def CalculateSalary(self):
        return self._hourlySalary * self._hoursWorked


class SalesmanEmployee(Employee):
    def __init__(self,namn, birthDate,accountNo, monthlySalary, soldFor):
        super().__init__(namn,birthDate,accountNo)
        self._monthlySalary = monthlySalary
        self._soldFor = soldFor

    def CalculateSalary(self):
        return self._monthlySalary + self._soldFor * 0.02


    
lista = []

e = MonthlyEmployee("Stefan", datetime.date(1972,8,3),"12345",12000);
lista.append(e)

e = MonthlyEmployee("Kerstin", datetime.date(1973,8,3),"12132",11000)
lista.append(e)

e = HourlyEmployee("Fanny", datetime.date(2000,1,2),"74384794-23443",20,130)
lista.append(e)

e = SalesmanEmployee("Josefine", datetime.date(2002,3,30),"23423443",6000,8000)
lista.append(e)



e = Employee("David", datetime.date(2002,3,30),"12345")
lista.append(e)




for employee in lista:
    print(employee.CreateSalaryTransaction())