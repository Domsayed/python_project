class Employee:
        def __init__(self,first,last,pay):
                self.first=first
                self.last=last
                self.pay=pay
                self.email=first+'.'+last+'@company'
        def fullname(self):
                return'{}{}'.format(self.first,self.last)
        def apply_raise(self):

                self.pay=int(self.pay*1.04)
        
emp_1=Employee('rahil','khan',25000)
emp_2=Employee('jon','son',12345)
print(emp_1.pay)
emp_1.apply_raise()
Employee.raised_ammount=2
print(emp_1.__dict__)
print(Employee.__di
