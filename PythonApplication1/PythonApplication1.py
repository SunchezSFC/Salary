# -*- coding: utf-8 -*-
# ���������� � ����������� � �� ��������
# ������� ��� ���������� ����������
def add_employee(employees):
    name = input("������� ��� ����������: ")
    salary = float(input("������� �������� ����������: "))
    employees[name] = salary

# ������� ��� ������ ���������� � ����������� � �� ��������
def get_employee_info(employees):
    for name, salary in employees.items():
        print(f"{name}: {salary}")

# ������� ��� ���������� ���������� � ����������� � �� ��������
def get_employee_statistics():
    employees = {}
    choice = ""
    while choice != "4":
        print("1. �������� ����������")
        print("2. ������� ���������� � ����������� � �� ��������")
        print("3. ������� ���������� � �������� � �� �����������")
        print("4. �����")
        choice = input("��� �����: ")
        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            get_employee_info(employees)
        elif choice == "3":
            for salary, employees_list in sorted(employees.items(), reverse=True):
                print(f"�������� {salary}:")
                for name in employees_list:
                    print(f"- {name}")
                print()
        elif choice == "4":
            print("�� ��������!")
        else:
            print("�������� �����.")

# ������ ����������
get_employee_statistics()
