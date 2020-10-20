#define directions function
def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

#define menu function
def menu():
  print("Please select a direction")
  selection = directions()
  for index in range(len(selection)):
    print("{}: {}".format(index,selection[index]))
  direction_index = int(input())
  return selection[direction_index]

#define the fun function
def run():
  route = []
  print("Working out escape route...")
  for count in range(5):
    direction = menu()
    route.append(direction)
  print("Escape route: {}".format(route))


run()
