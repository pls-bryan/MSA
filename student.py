class Student:
    def __init__(self, first_name, last_name, major, credit_hours, gpa, id_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id_number = id_number
        self.__major = major
        self.__credit_hours = credit_hours
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
    
    def get_credit_hours(self):
        return self.__credit_hours

    def set_credit_hours(self, credit_hours):
        self.__credit_hours = credit_hours

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def get_class_level(self):
        if float(self.__credit_hours) > 90:
            return "Senior"
        elif float(self.__credit_hours) > 60:
            return "Junior"
        elif float(self.__credit_hours) > 30:
            return "Sophomore"
        else:
            return "Freshman"

    def update_credit_hours(self, additional_hours):
        self.__credit_hours += additional_hours
