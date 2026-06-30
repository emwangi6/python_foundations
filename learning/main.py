import student
from student import Student

s1 = Student('Ephantus',20,'BBIT',223464)
s2 = Student('John',19,'BBIT',223468)
s3 = Student('John',19,'BBIT',223468)
s4 = Student('John',19,'BBIT',223468)

print(s1.name)
print(s1.age)
print(s1.course)
print(s1.adm)
s1.introduce()
#Access a class variable by the class name
print(Student.class_year)
print(Student.num_students)
