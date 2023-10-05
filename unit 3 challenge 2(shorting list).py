class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Create a list of 5 student objects for testing
students = [
    Student("motu", "A123", 4.8),
    Student("hatori", "B456", 3.5),
    Student("nobita", "C789", 3.9),
    Student("Doraemon", "D234", 3.2),
    Student("benten", "J234", 3.3)
]

# Sort the list of students by CGPA
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
