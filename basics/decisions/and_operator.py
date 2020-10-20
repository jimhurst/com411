def run():  
  #input - what was heard
  print("What did I hear?")
  hear = input()
  #input - what was seen
  print("What did I see?")
  see = input()
  #logic and output
  if ((hear.lower() == "grrr") and (see.lower() == "two red eyes")):
    print("There is a scary creature. I should get out of here!")
  else:
    print("I am a little scared but I will continue")