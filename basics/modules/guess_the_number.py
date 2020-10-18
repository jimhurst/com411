def run():
  #user input
  print("Please enter the minimum value")
  minval = int(input())
  print("Please enter the maximum value")
  maxval = int(input())
  print("Ok, I am thinking of a number between {} and {}".format(minval, maxval))


  import random as rnd
  randomgen = rnd.randrange(minval, maxval)

  choice = -1
  while (choice != randomgen):
    print("Ok have a guess...")
    choice = int(input())
    if choice == randomgen:
      print("Nice guess.... awesome work")
    elif choice < randomgen:
      print("Close, but a little to low")
    else:
      print("hmmm that's too high, come down a bit")

  print("<------ GAME OVER ------>") 

