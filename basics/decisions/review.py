def run():
  #PLANET QUIZ
  #Q1
  print("How many planets are in our solar system?")
  numplanets = input()
  score = 0
  if ((numplanets == "8") or (numplanets == "9")):
    print("nicely done, pluto is now classified as a dwarf planet so the answer is technically 8")
    score = score + 1
  elif ((numplanets == "7") or (numplanets == "10")):
    print("Well that is close, but not close enough")
  else:
    print("no I am afraid that is not right")
  #Q2
  print("what is the biggest planet?")
  planet1 = input()
  if planet1 == "Jupiter":
    print("absolutely correct")
    score = score + 1
  #Q2 - Second Chance To Guess!
  elif planet1 == "Saturn":
    print("that is close, Saturn is the second biggest so try again")
    print("what is your second guess?")
    planet1a = input()
    if planet1a == "Jupiter":
      print("Yes that's right")
      score = score + 1
    else:
      print("I am afraid that is wrong")
  else:
    print("WRONG!!!")
  #Q3
  print("name any planet other than the first to orbit our sun")
  orbit = input()
  if ((orbit != "Mercury") and (orbit == "Venus") or (orbit == "Earth") or (orbit == "Mars") or (orbit == "Jupiter")  or (orbit == "Saturn") or (orbit == "Uranus")  or (orbit == "Neptune")):
    print("Nice one")
    score = score + 1
  else:
    print("Better luck next time")
  #FINAL SCORE
  print("")
  print(f"You have scored a total of {score}")