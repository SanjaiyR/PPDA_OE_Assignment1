import os
employees_file = 'employees.txt'
performance_file = 'performance.txt'

def load_data(file_path):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as file:
        data = file.readlines()
    return {line.split(':')[0]: line.split(':')[1].strip() for line in data}

def save_data(file_path, data):
    with open(file_path, 'w') as file:
        for key, value in data.items():
            file.write(f'{key}:{value}\n')

def add_employee(employees):
    emp_id = input('Enter employee ID: ')
    name = input('Enter employee name: ')
    department = input('Enter department: ')
    salary = input('Enter salary: ')
    employees[emp_id] = f'{name},{department},{salary}'
    print('Employee added successfully.')

def update_employee(employees):
    emp_id = input('Enter employee ID to update: ')
    if emp_id not in employees:
        print('Employee not found.')
        return
    name = input('Enter new employee name: ')
    department = input('Enter new department: ')
    salary = input('Enter new salary: ')
    employees[emp_id] = f'{name},{department},{salary}'
    print('Employee record updated successfully.')

def calculate_salary(employees):
    emp_id = input('Enter employee ID: ')
    if emp_id not in employees:
        print('Employee not found.')
        return
    details = employees[emp_id].split(',')
    salary = float(details[2])
    bonus = salary * 0.10 
    print(f"Employee ID: {emp_id}")
    print(f"Name: {details[0]}")
    print(f"Department: {details[1]}")
    print(f"Salary: {salary}")
    print(f"Bonus: {bonus}")
    print(f"Total Compensation: {salary + bonus}")

def main():
    employees = load_data(employees_file)
    performance = load_data(performance_file)

    while True:
        print("\nEmployee Management System")
        print("1. Add employee")
        print("2. Update employee record")
        print("3. Calculate salary and bonus")
        print("4. Exit")
        choice = input('Enter your choice: ')

        if choice == '1':
            add_employee(employees)
            save_data(employees_file, employees)
        elif choice == '2':
            update_employee(employees)
            save_data(employees_file, employees)
        elif choice == '3':
            calculate_salary(employees)
        elif choice == '4':
            print('Exiting the system.')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
