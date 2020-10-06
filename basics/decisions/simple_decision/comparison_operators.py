#as for the users first choice
print("ok make your first choice, pick a number")
first = int(input())
print(f"nice choice, so you have gone with {first} as your first number")
#as for the users second choice
print("ok now make your second choice, go ahead and pick a number")
second = int(input())
print(f"cool, so you have gone with {second} as your second number")
#calculations & output
print("let me work this out....")
if first > second:
  print("Ok, looks like the first number is the biggest")
elif first < second:
  print("looks to me like the second number is bigger")
else:
  print("you are trying to trick me, they are the same!")