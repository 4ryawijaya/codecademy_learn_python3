class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    self.attendance = {}
  
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)
    else:
       raise ValueError("Invalid grade type data")
    
  def get_average(self):
    average = sum(grade.score for grade in self.grades) / len(self.grades)
    return average

  def get_attendance(self, date):
    self.attendance = {self.name: self.date}
    return self.attendance


class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score

  def is_passing(self):
    return self.score >= self.minimum_passing
     

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

grade1 = Grade(100)
grade2 = Grade(45)

pieter.add_grade(grade1)
pieter.add_grade(grade2)

average = pieter.get_average()

for grade in pieter.grades:
  if grade.is_passing():
    print("{} with the score {}, congratulation you passed!".format(pieter.name, grade.score))
  else:
    print("{} with the score {}, you failed, try again!".format(pieter.name, grade.score))

print("{} average score is {}".format(pieter.name, average))

# pieter.add_grade(Grade.is_passing(100))