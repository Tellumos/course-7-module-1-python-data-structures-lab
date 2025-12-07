def student_generator(student_list, major):

    return (student for student in student_list if major.lower() in student[2].lower())
