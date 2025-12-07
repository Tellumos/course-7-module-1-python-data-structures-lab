def filter_students_by_major(student_list, major):
    return [student for student in student_list if major.lower() in student[2].lower()]
