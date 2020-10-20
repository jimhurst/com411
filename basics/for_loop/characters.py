def run():
  #Ask for user input and store in variable
  print("What strange markings do you see?")
  strange_input = input()
  print("Identifying....")
  print("")
  for position in range (0, len(strange_input),1):
    print(f"Index {position}:", strange_input[position])
  print("")
  print("All Done!")
