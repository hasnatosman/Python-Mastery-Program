# OOP Principles
# Advanced concepts of object-oriented programming.
# Encapsulation
# Protecting data inside classes
# Inheritance
# Creating child classes
# Reusing parent class code
#
# Polymorphism
# Method overriding
# Same interface different behavior
# Abstraction
# Abstract classes
# Hiding complex implementation
# Practice:
# Employee management system

# Encapsulation (Data protection): keep data private, access via methods(get/set)

# class Employee:
#     def __init__(self, name: str, salary: float):
#         self.name  = name              # public
#         self.__salary = salary         # private (encapsulated)
#
#     def get_salary(self) -> float:
#         return self.__salary
#
#     def set_salary(self, new_salary: float) -> None:
#         if new_salary > 0:
#             self.__salary = new_salary
#         else:
#             raise ValueError("Salary must be positive")
#
#
# # Inheritance (Code resue): Child class reuses parent class
#
# class Manager(Employee):                 # Manager inherits from Employee
#     def __init__(self, name: str, salary: float, department: str):
#         super().__init__(name, salary)       # super(): calls parent constructor
#         self.department = department


# Polymorphism (Same interface, different behavior): same method, different behavior

# class Developer(Employee):
#     def calculate_bonus(self) -> float:
#         return self.get_salary() * 0.10
# class Manager(Employee):
#     def __init__(self, name: str, salary: float, department: str):
#         super().__init__(name, salary)
#         self.department = department
#
#
#     def calculate_bonus(self) -> float:
#         return self.get_salary() * 0.20


# Abstraction (Hide Complexity): define structure, hide implementation

# from abc import ABC, abstractmethod
#
# class BaseEmployee(ABC):
#
#     @abstractmethod
#     def calculate_bonus(self) -> float:
#         pass



# Practice
# Employee Management System


from abc import ABC, abstractmethod

class BaseEmployee(ABC):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.__salary = salary

    def get_salary(self) -> float:
        return self.__salary

    def set_salary(self, new_salary: float) -> None:
        if new_salary > 0:
            self.__salary = new_salary
        else:
            raise ValueError('Invalid Salary')

    @abstractmethod
    def calculate_bonus(self) -> float:
        pass

class Developer(BaseEmployee):
    def calculate_bonus(self) -> float:
        return self.get_salary() * 0.10

class Manager(BaseEmployee):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department
    def calculate_bonus(self) -> float:
        return self.get_salary() * 0.20

# Usage
employees = [
    Developer(name = 'Hasnat', salary=50000),
    Manager(name='Rahim', salary=80000, department= 'IT')
]

for employee in employees:
    print(f'Name: {employee.name}')
    print(f'Salary: {employee.get_salary()}')
    print(f'Bonus: {employee.calculate_bonus()}')
    print('-' * 20)
