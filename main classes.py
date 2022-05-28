class Student():
#lassignment) Skeleton class. Add your code here
  def __init__(self, name, age, tracks, score):
    self.name = name
    self.age age self.tracks tracks
    self.score score
    pass

  def change_name(self, new_name):
    self.name= new_name

  def change_age(self,new_age):
    self.age = new age

  def add_track(self,new_track):
    self.tracks = new_track

  def get_score(self):
    if is instance(self.age,int):
      print(self.name, self.age,self.tracks, self.score)
    else:
      print("Age must be int. please try again")

Lex = Student (name="Lex", age=24, tracks=["FE", "BE"],score=20.98)

# Expected methods
Lex.change_name("John")
Lex.add_track("UI/UX")
Lex.change_age(34)
Lex.get_score()
