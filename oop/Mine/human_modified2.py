class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0

  # An instance method
  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'


   
class Human:
  # A class attribute
  MAX_ENERGY = 100

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Human"
    self.age = 0
    self.energy = 0

  # An instance method
  def display(self):
    print(f"I am {self.name} and my age is {self.age} and my energy is {self.energy}")

  # An instance method - Eat (Increase Energy)
  def eat(self, increase):
    if self.energy + increase > Human.MAX_ENERGY:
      print("It is not possible to exceed the maximum energy value of 100")
    else:
      self.energy = self.energy + increase

  # An instance method - Move (Decrease Energy)
  def move(self, distance):
    if self.energy - distance < 0:
      print("It is not possible to go below an energy value of 0, please reduce the length of the move")
    else:
      self.energy = self.energy - distance

  # An instance method - Increase Age By 1
  def grow(self):
    self.age += 1
    

#Test Area
if (__name__ == "__main__"):
  my_robot = Robot()
  print(repr(my_robot))

if (__name__ == "__main__"):
  my_human = Human()
  my_human.eat(30)
  my_human.move(35)
  my_human.display()