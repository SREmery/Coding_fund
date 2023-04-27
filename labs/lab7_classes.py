class Student:
    def __init__(self, name, age, class_="student"):
        self.name = name
        self.age = age
        self.class_ = class_

    def av_mark(self, score1, score2, score3):
        x = (score1 + score2 + score3) / 300 * 100
        return f"{self.name}, your average test mark is {x}%"

student_1 = Student("John", 16)

print(student_1.av_mark(30, 90, 50))

print(student_1.name, "is", student_1.age)





