class Student:
    #class variable -> shared among all instances of a class
    #                  defined outside the constructor
    #                  Allow sharing of data among all object created from that class
    class_year = 2029 # Class Variable
    num_students = 0
    def __init__(self,name,age,course,adm):
        self.name=name
        self.age=age # Instance variable
        self.course=course
        self.adm =adm
        Student.num_students += 1

    def introduce(self):
        print(f'I am called {self.name}')

