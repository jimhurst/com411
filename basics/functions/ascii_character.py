#user input
print("Program Started!")
print("Please enter an ASCII code")
#store to variable as integer
code = abs(int(input()))
#set variables to use with range
lowv = 32
highv = 127
#check that input is within range and execute ord command to lookup
if code in range(lowv, highv):
  letter = chr(code)
  print("The character represented by the ASCII code {} is {}".format(code,letter))
else:
  print("The value entered is outside of the ASCII code range")
#program end message
print("Program Ended!")
