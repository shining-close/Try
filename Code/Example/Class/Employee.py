class Employee:

    status = "current employee"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        print("Name:", self.name, "\nAge:", self.age, "\nGender", self.gender)

    def course_taught(self, course):
        return "{} teaches {}.".format(self.name, course)
    
class PartTimeEmployee(Employee):
    def number_hours(self, hours):
        return "{} works for {} pre week.".format(self.name, hours)
    
class FullTimeEmployee(Employee):
    def number_hours(self, hours):
        return "{} works for {} pre week.".format(self.name, hours)
    
mireilla = FullTimeEmployee("Mireilla", 46, "Female")
print(mireilla.info())

print(mireilla.number_hours(40))

print(isinstance(mireilla, Employee))

paul = Employee("Paul", 49, "Male")
print(isinstance(paul, Employee))

cristina = PartTimeEmployee("Cristina", 21, "Female")
print(isinstance(cristina, FullTimeEmployee))

print(isinstance(paul, mireilla))