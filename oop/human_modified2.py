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
  

#Test - Runs code if not being imported
if (__name__ == "__main__"):
  my_robot = Robot()
  print(repr(my_robot))
  
class Human:
  # A class attribute
  MAX_ENERGY = 100

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  # An instance method
  def display(self):
    print(f"I am {self.name} and my age is {self.age} and my energy is {self.energy}")
    

#Test - Runs code if not being imported
if (__name__ == "__main__"):
  human = Human()
  human.display()
