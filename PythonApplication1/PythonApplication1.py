# -*- coding: utf-8 -*-
# Информация о сотрудниках и их зарплате
# Функция для добавления сотрудника
def add_employee(employees):
    name = input("Введите имя сотрудника: ")
    salary = float(input("Введите зарплату сотрудника: "))
    employees[name] = salary

# Функция для вывода информации о сотрудниках и их зарплате
def get_employee_info(employees):
    for name, salary in employees.items():
        print(f"{name}: {salary}")

# Функция для вычисления информации о сотрудниках и их зарплате
def get_employee_statistics():
    employees = {}
    choice = ""
    while choice != "4":
        print("1. Добавить сотрудника")
        print("2. Вывести информацию о сотрудниках и их зарплате")
        print("3. Вывести информацию о зарплате и их сотрудниках")
        print("4. Выход")
        choice = input("Ваш выбор: ")
        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            get_employee_info(employees)
        elif choice == "3":
            for salary, employees_list in sorted(employees.items(), reverse=True):
                print(f"Зарплата {salary}:")
                for name in employees_list:
                    print(f"- {name}")
                print()
        elif choice == "4":
            print("До свидания!")
        else:
            print("Неверный выбор.")

# Запуск приложения
get_employee_statistics()
