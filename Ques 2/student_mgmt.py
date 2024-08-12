import os
students_file = 'students.txt'
courses_file = 'courses.txt'
grades_file = 'grades.txt'
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

def add_student(students):
    student_id = input('Enter student ID: ')
    name = input('Enter student name: ')
    age = input('Enter student age: ')
    students[student_id] = f'{name},{age}'
    print('Student added successfully.')

def enroll_student(students, courses):
    student_id = input('Enter student ID: ')
    course_name = input('Enter course name: ')
    if student_id not in students:
        print('Student not found.')
        return
    if student_id not in courses:
        courses[student_id] = []
    courses[student_id].append(course_name)
    print('Student enrolled in course successfully.')

def calculate_grades(grades):
    student_id = input('Enter student ID: ')
    if student_id not in grades:
        print('No grades found for this student.')
        return
    student_grades = grades[student_id]
    total = sum(student_grades.values())
    average = total / len(student_grades)
    print(f'Average grade for student {student_id}: {average}')

def main():
    students = load_data(students_file)
    courses = load_data(courses_file)
    grades = load_data(grades_file)  # Assuming grades are in the format of student_id:course=grade

    while True:
        print("\nStudent Management System")
        print("1. Add student")
        print("2. Enroll student in course")
        print("3. Calculate grades")
        print("4. Exit")
        choice = input('Enter your choice: ')

        if choice == '1':
            add_student(students)
            save_data(students_file, students)
        elif choice == '2':
            enroll_student(students, courses)
            save_data(courses_file, courses)
        elif choice == '3':
            calculate_grades(grades)
        elif choice == '4':
            print('Exiting the system.')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
