class Employee:
    employees = []
    
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        self.salary = 3000 
        Employee.employees.append(self)
    
    def calculate_salary(self):
        return self.salary 
    
    def show_details(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: ${self.calculate_salary()}")
    
    @staticmethod
    def list_employees():
        if not Employee.employees:
            print("No employees available.")
        else:
            print("\nList of Employees:")
            for emp in Employee.employees:
                emp.show_details()


class Manager(Employee):
    BONUS_PERCENTAGE = 0.2  
    
    def calculate_salary(self):
        return self.salary + (self.salary * self.BONUS_PERCENTAGE)


class Engineer(Employee):
    PERFORMANCE_BONUS = 0.1  
    
    def calculate_salary(self):
        return self.salary + (self.salary * self.PERFORMANCE_BONUS)


class Intern(Employee):
    def calculate_salary(self):
        return self.salary 


while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Manager")
    print("2. Add Engineer")
    print("3. Add Intern")
    print("4. Show Employee List")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice in ["1", "2", "3"]:
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        
        if choice == "1":
            Manager(name, emp_id)
            print("Manager added successfully!")
        elif choice == "2":
            Engineer(name, emp_id)
            print("Engineer added successfully!")
        elif choice == "3":
            Intern(name, emp_id)
            print("Intern added successfully!")
    elif choice == "4":
        Employee.list_employees()
    elif choice == "5":
        print("Thank you for using the Employee Management System!")
        break
    else:
        print("Invalid option! Please try again.")
