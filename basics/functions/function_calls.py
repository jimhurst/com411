#displaybox function
def displaybox(word):
  num_dashes = 4 + len(word)
  print("-" * num_dashes)
  print("| {} |".format(word))
  print("-" * num_dashes)

#display lower case function
def lower(word):
  print(word.lower())

#display upper case function
def upper(word):
  print(word.upper())

#display repeat function
def repeat(word):
  print("How many times would you like to repeat your word -- {} --".format(word))
  repeatcount = int(input())
  for seq in range(repeatcount):
    #even repetition
    if (seq % 2 == 0):
      print(word.lower())
    else:
      print(word.upper())
  
#display mirrored
def dismirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print("{} | {}".format(word, mirrored))



#user input for word
print("Choose a word")
word = input()

choice = 0
while (choice != 6):
  #user input for function choice
  print("choose a function from the below")
  print("[1] Display Box")
  print("[2] Lowercase")
  print("[3] Uppercase")
  print("[4] Repeat")
  print("[5] Reverse")
  print("[6] Exit")

  choice = int(input())

  if (choice == 1):
    displaybox(word)
  elif (choice == 2):
    lower(word)
  elif (choice == 3):
    upper(word)
  elif (choice == 5):
    dismirrored(word)
  elif (choice == 4):
    repeat(word)
  elif (choice == 6):
    break



