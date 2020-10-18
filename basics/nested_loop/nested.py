def run():
  #user input for number of rows
  print("How many rows should I have?")
  rows = int(input())
  #user input for number of columns
  print("How many columns should I have?")
  columns = int(input())
  #render output
  for row in range (0,rows,1):
    for column in range (0,columns,1):
      print(":-", end="")
    print()