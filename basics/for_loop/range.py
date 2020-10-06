#establish the brightness required
print("What level of brightness is required")
brightness = int(input())
#use for and range command to render brightness incriments
for adjustb in range (2, brightness + 1,2):
  print("Adjusting brightness.....")
  print("Beep's Brightness Level:", "✠" * adjustb)
  print("Bop's Brightness Level:", "✠" * adjustb)