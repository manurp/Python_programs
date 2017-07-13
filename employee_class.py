class Employee:
	num_of_emps=0
	raise_amt=1.04

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		#self.email=first+"."+last+"@company.com"
		self.pay=pay

		Employee.num_of_emps+=1
	#def fullname(self):
	#	return '{} {}'.format(self.first,self.last)
	
	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first,self.last)
		
	@property
	def fullname(self):
		return '{} {}'.format(self.first,self.last)
		
	@fullname.setter
	def fullname(self,name):
		first,last=name.split()
		self.first,self.last=first,last
		
	@fullname.deleter
	def fullname(self):
		self.first,self.last=None,None
	
	def apply_raise(self):
		self.pay=self.pay*self.raise_amt
		
	@classmethod
	def set_raise_amount(cls,amount):
		cls.raise_amt=amount

	@classmethod
	def from_string(cls,emp_str):
		first,last,pay=emp_str.split('-')
		return cls(first,last,pay)

	@staticmethod
	def is_workday(day):
		if day.weekday()==5 or day.weekday()==6:
			return False
		return True
		
	def __add__(self,other):
		return self.pay+other.pay
		
	def __repr__(self):
		return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)
		
	def __str__(self):
		return "{}-{}".format(self.fullname,self.email)

class Developer(Employee):
	raise_amt=1.10

	def __init__(self,first,last,pay,prog_lang):
		#super().__init__(first,last,pay)
		#super().__init__(first,last,pay) #Works fine with python3
		Employee.__init__(self,first,last,pay)
		self.prog_lang=prog_lang

class Manager(Employee):

	def __init__(self,first,last,pay,employees=None):
		#Employee.__init__(self,first,last,pay)
		super().__init__(first,last,pay)
		if employees==None:
			self.employees=[]
		else:
			self.employees=employees

	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(employees)

	def print_emp(self):
		for emp in self.employees:
			print('-->',emp.fullname)

emp1=Employee("Manoj","Poojari",50000)
emp2=Employee("Bhoomika","Poojari",60000)

print(emp1.fullname)
print(emp2.fullname)

emp1.apply_raise()
print(emp1.pay)

Employee.set_raise_amount(1.06)#can be objects i.e., emp1.set_raise_amount
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

emp1_str='Ravi-Kumar-30000'
emp2_str='Shamantha-Ravi-40000'

new_emp1=Employee.from_string(emp1_str)
print(new_emp1.email)

import datetime
my_date=datetime.date(2017,6,25)
print(emp2.is_workday(my_date))#can be Employee.is_workday(..)
print("")

dev1=Developer('Rohit','Prasad',50000,'Python')
dev2=Developer('Anurag','Sampath',60000,'Java')

print(dev1.email)

mgr=Manager('Veena R','Bhatt',70000,[emp1])
print(mgr.fullname)
mgr.print_emp()
mgr.add_emp(dev1)
mgr.print_emp()
#print(help(Manager))

print(emp1+emp2) #__add__
print(emp1)
print(repr(emp2))

emp1.fullname ='ManojR Poojari'
print(emp1.fullname)
del emp1
# print(dev1.is_workday(my_date))#
# print(emp1)
emp1=Employee('Manoj','Poojari',60000)
print(emp1) #__str__ if no __str__ then calls __repr__