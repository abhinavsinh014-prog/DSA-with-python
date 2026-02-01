student_name = input("Enter student name: ")
student_marks = {
    "Aditi": 98,
    "Abhinav": 92,
    "Randy": 78,
    "John": 95,
    "Pandat": 27,
    "Gadariya": 90,
    "Mohit": 82,
    "Mota": 25
}
if student_name in student_marks:
    print(f"Student {student_name} has marks: {student_marks[student_name]}")
    if student_marks[student_name] < 33:
        print("status Fail")
    else:
        print("status Pass")    

else:
    print("Student not found in records.")