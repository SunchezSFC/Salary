import json

class Employee:
    def __init__(self, id, name, surname, patronymic, gender, birth_date, position, salary):
        self.id = id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.gender = gender
        self.birth_date = birth_date
        self.position = position
        self.salary = salary

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_employee_by_id(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                return employee
        return None

    def update_employee(self, employee_id, updated_employee):
        for i, employee in enumerate(self.employees):
            if employee.id == employee_id:
                self.employees[i] = updated_employee
                return True
        return False

    def delete_employee(self, employee_id):
        for i, employee in enumerate(self.employees):
            if employee.id == employee_id:
                del self.employees[i]
                return True
        return False

    def save_to_file(self, file_name):
        with open(file_name, 'w') as file:
            json.dump([employee.__dict__ for employee in self.employees], file)

    def load_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                for employee_data in data:
                    self.add_employee(Employee(**employee_data))
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден.")

employee_manager = EmployeeManager()

# Пример добавления сотрудника
employee_manager.add_employee(Employee(1, 'Иван', 'Иванов', 'Иванович', 'М', '01.01.1990', 'Разработчик', 50000))

# Пример получения сотрудника по ID
employee = employee_manager.get_employee_by_id(1)
print(employee.name)  # Выведет: Иван

# Пример обновления информации о сотруднике
updated_employee = Employee(1, 'Иван', 'Иванов', 'Иванович', 'М', '01.01.1990', 'Старший разработчик', 60000)
employee_manager.update_employee(1, updated_employee)

# Пример удаления сотрудника
employee_manager.delete_employee(1)

# Пример сохранения данных в файл
employee_manager.save_to_file('employees.json')

# Пример загрузки данных из файла
employee_manager.load_from_file('employees.json')
