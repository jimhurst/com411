def run():
  #user inputs their three number choices
  print("Please enter your first number")
  first = int(input())
  print("Please enter your second number")
  second = int(input())
  print("Please enter your third number")
  third = int(input())
  #calculations stored in new variables
  calc1 = first % 2
  calc2 = second % 2
  calc3 = third % 2
  #odd and even variables established and set to zero
  odd = 0
  even = 0
  #logic to perform odd and even number counting operations
  if calc1 != 0:
    odd = odd + 1
  else:
    even = even + 1
  if calc2 != 0:
    odd = odd + 1
  else:
    even = even + 1
  if calc3 != 0:
    odd = odd + 1
  else:
    even = even + 1
  #producing the output
  print(f"Looks like you entered {even} even and {odd} odd numbers")



