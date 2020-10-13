print("Program Started!")
print("Please enter a standard character")
char = input()
if len(char) == 1:
  print(f"The ASCII code for {char} is", ord(char))
else:
  print("you entered more than one character")
print("Program Ended!")
