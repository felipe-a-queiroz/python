from employee import Employee, SalaryEmployee, HourlyEmployee, ComissionEmployee

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current employees:')
        for employee in self.employees:
            print(employee.fname, employee.lname)
        print('----------')
    
    def pay_employees(self):
        print('Paying employees:')
        for employee in self.employees:
            print('Paying check for:', employee.fname, employee.lname)
            print(f'Amount: ${employee.calculate_paycheck():,.2f}')
        print('----------')


def main():
    my_company = Company()

    employee1 = SalaryEmployee('Sarah', 'Hess', 50000)
    my_company.add_employee(employee1)

    employee2 = HourlyEmployee('Lee', 'Smith', 25, 20)
    my_company.add_employee(employee2)

    employee3 = ComissionEmployee('Bob', 'Brown', 30000, 5, 200)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()