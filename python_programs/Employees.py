class Employees:
	def __init__(self, name, role, status, salary):
		self.name = name
		self.role = role
		self.status = status
		self.salary = salary
		
	def eligible_for_increment(self):
		return self.salary < 2000;
