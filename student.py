class Student:
    def __init__(self, first_name, last_name, id_number, major, grade_level, gpa):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id_number = id_number
        self.__major = major
        self.__grade_level = grade_level
        self.__gpa = gpa
    
    def get_first_name(self):
        return self.__first_name
    
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_id_number(self):
        return self.__id_number
    
    def get_major(self):
        return self.__major

    def set_major(self, major):
        self.__major = major
    
    def get_grade_level(self):
        return self.__grade_level

    def set_grade_level(self, grade_level):
        self.__grade_level = grade_level

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa

    
