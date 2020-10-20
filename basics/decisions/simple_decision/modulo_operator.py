def run():
  #ask user for whole number input
  print("Please enter a whole number of your choice")
  whole = int(input())
  calc = whole % 2
  if calc != 0:
    print(f"the number {whole} is an odd number")
  else:
    print(f"the number {whole} is an even number")