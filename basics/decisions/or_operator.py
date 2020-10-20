def run():
  #input to determine adventure type
  print("what type of adventure do you want")
  storytype = input()
  #if scary or short
  if ((storytype == "scary") or (storytype == "short")):
    print("you are entering the dark forest!")
  #if safe or long
  elif ((storytype == "safe") or (storytype == "long")):
    print("you are taking the safe route")
  #else
  else:
    print("I don't know which route to take")