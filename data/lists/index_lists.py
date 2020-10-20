#define movement function
def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

#define the run function
def run():
  print("Moving...")
  direction = movements()
  for index in range(0, len(direction), 2):
   print("{} for {} steps".format(direction[index],direction[index+1]))

run()

#repetative solution to the define run function
  #print("{} for {} steps".format(direction[0],direction[1]))
  #print("{} for {} steps".format(direction[2],direction[3]))
  #print("{} for {} steps".format(direction[4],direction[5]))
  #print("{} for {} steps".format(direction[6],direction[7]))