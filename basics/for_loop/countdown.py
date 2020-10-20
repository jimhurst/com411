def run(): 
  #User input on how far from the cave
  print("How far are we from the cave?")
  cavecount = int(input())
  #counting down the remaining steps
  for count in range(cavecount):
    print(f"There are {cavecount} steps remaining")
    cavecount = cavecount - 1
  print("")
  print("We have reached the cave!!!")