#define directions function
def directions():
  path = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return path

#define menu function
def menu():
  print("Please select a direction")
  selection = directions()
  for index in range(len(selection)):
    print("{}: {}".format(index,selection[index]))

#define the fun function
def run():
  menu()

run()