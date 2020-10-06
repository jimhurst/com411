#ask user to input a sequence and specify the markers they have used
print("enter a sequence of your choice, and include markers")
sequence = input()
print("tell me what character you have used for the markers")
marker = input()
#find the markers!
marker1_position = -1
marker2_position = -1
for position in range(0,len(sequence),1):
  letter = sequence[position]
  if (letter == marker):
    if (marker1_position == -1):
      marker1_position = position
    else:
      marker2_position = position
#display the output
print("the distance between the markers is", marker2_position - marker1_position - 1)



