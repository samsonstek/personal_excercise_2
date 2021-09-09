class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Calculating Payroll")
        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculate_payroll()}")
            print("")
#Employee is the base class for all employee types
#All employees have name and id 
class Employee:
    def __init__(self, name, id):
        self.name= name
        self.id = id
#The first type of employees are the ones with weekly fixed salary
class SalaryEmployee(Employee):
    def __init__(self, name, id, weekly_salary):
        super().__init__(name, id)
        self.weekly_salary= weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary
#The second type are the ones who are paid by the hour
#We calculate their payroll by multiplying their hourly rate by hours worked
class HourlyEmployee(Employee):
    def __init__(self, name, id, hours_worked, hourly_rate):
        super().__init__(name, id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate
#The third type are paid weekly salary and commission
class CommissionEmployee(SalaryEmployee):
    def __init__(self, name, id, weekly_salary, commission):
        super().__init__(name, id, weekly_salary)
        self.commission = commission
    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission

salary_employee= SalaryEmployee(1,"Samson Seged", 2500)   
hourly_employee = HourlyEmployee(2, "Halle Berry", 1000, 250)
commission_employee = CommissionEmployee(3, "Allison Perry", 1000, 250)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,hourly_employee,commission_employee])


