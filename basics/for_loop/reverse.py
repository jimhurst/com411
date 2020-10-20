def run():
  print("Ok, what phrase do you see?")
  phrase = input()
  print("Ok, let me reverse that for you.....")
  for position in range (len(phrase) -1, -1, -1):
    print(phrase[position], end="")