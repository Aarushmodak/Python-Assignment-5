# Task 1: Create a Dictionary of Student Marks

stu_details = {'carol': 90, 'alice': 85}

name = input("Enter the student's name: ").strip()

print(f"{name.title()}'s marks: {stu_details[name.lower()]}" if name.lower() in stu_details else "Student not found.")
