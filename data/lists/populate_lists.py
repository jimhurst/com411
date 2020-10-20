#define directions function
def directions():
<<<<<<< HEAD
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions
=======
  path = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return path
>>>>>>> 1600ea76d2e60d8ae3ebd5d49029d91a7e0552f6

#define menu function
def menu():
  print("Please select a direction")
  selection = directions()
  for index in range(len(selection)):
    print("{}: {}".format(index,selection[index]))
<<<<<<< HEAD
  direction_index = int(input())
  return selection[direction_index]
=======
  response = int(input())
  return selection[response]
>>>>>>> 1600ea76d2e60d8ae3ebd5d49029d91a7e0552f6

#define the fun function
def run():
  route = []
  print("Working out escape route...")
<<<<<<< HEAD
  for count in range(5):
    direction = menu()
    route.append(menu())
  print("Escape route: {}".format(route))

=======
  for index in range(1):
      menu()
      route.append(menu())
  print(menu())
>>>>>>> 1600ea76d2e60d8ae3ebd5d49029d91a7e0552f6

run()