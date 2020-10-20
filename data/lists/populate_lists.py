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
  response = int(input())
  return selection[response]

#define the fun function
def run():
  route = []
  print("Working out escape route...")
  for index in range(1):
      menu()
      route.append(menu())
  print(menu())

run()