#asking user who is the better doctor
print("Who is the better doctor, Tom or Jon?")
bestdoc = input()
#if they chose Tom, asking which assistant is better and using if to respond
if bestdoc == 'Tom':
  print("good choice, did you prefer Louise or Romana as the assistant")
  assistant = input()
  if assistant == 'Louise':
    print("Yes I liked her too but Romana was better")
  else:
    print("Yes I agree, Louise wasn't as good")
    #sign off
print(f"ok so {bestdoc} is the best doctor")
    
