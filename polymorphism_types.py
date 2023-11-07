class Employee:
    __amt = 20000
    def sal(self):
        return self.__amt*2

class contractEmployee(Employee):
    __hrpay = 2000
    __hrs = 5
    def sal(self):
        return self.__hrpay*self.__hrs
emp=contractEmployee()
print(emp.sal())


