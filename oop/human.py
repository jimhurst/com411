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
  def display(self):
    print(f"I am {self.name}")

#Test - Runs code if not being imported
if (__name__ == "__main__"):
  robot = Robot()
  robot.display()


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
    print(f"I am {self.name}")

#Test - Runs code if not being imported
if (__name__ == "__main__"):
  human = Human()
  human.display()
