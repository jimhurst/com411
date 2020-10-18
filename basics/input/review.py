def run():
  #input into variables
  print("what is your age in years?")
  age = int(input())
  print("\n")
  print("Age:", "O" * age)
  print("\n")
  born = 2020 - age
  born2 = 2019 - age
  print(f"you were born in either {born} or {born2}")

