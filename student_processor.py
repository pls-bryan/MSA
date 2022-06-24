from student import Student

#load data from student csv file
#create objects for each student, and put objects in a list
#return the list
def load_students(csv_file):
    file = open(csv_file, "r")
    file_list = file.readlines()
    student_list = []
    counter = 1
    for x in range(1, len(file_list)):
        counter += 1
        file_split = file_list[x].split(",")
        if len(file_split) != 6:
            raise Exception(f"Data Error on line {counter}")
        student = Student(file_split[0], file_split[1], file_split[2], file_split[3], file_split[4], file_split[5])    
        student_list.append(student)
    return student_list

def print_data(student):
    print(f"Name: {student.get_first_name()} {student.get_last_name()}")
    print(f"ID: {student.get_id_number().strip()}")
    print(f"Major: {student.get_major()}")
    print(f"Credit Hours: {student.get_credit_hours()}")
    print(f"GPA: {student.get_gpa()}")
    print(f"Class Level: {student.get_class_level()}\n")
    
    
def main():
    load = load_students("students.csv")
    for x in load:
            print_data(x) 

main()
