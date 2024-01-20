class Student:
    group = "C2019"
    gender = "male"
    education = "MKA STEP"

    def __init__(self, name, age, swim):
        # print(id(self))
        self.name = name
        self.age = age
        self.swim = swim

    def get_swim(self):
        return self.swim


st1 = Student(name="Oleg", age=15, swim=True)
st2 = Student(name='Anna', age=14, swim=True)
st3 = Student(name='Ilya', age=16, swim=False)

print(st1.name, st1.get_swim())
print(st2.name, st2.get_swim())
print(st3.name, st3.get_swim())

# print(id(st1))
# st2 = Student()

# print(st1.group, st1.gender, st1.education)
# print(st2.group, st2.gender, st2.education)
# print()

# print(st1)
# print(st2)
