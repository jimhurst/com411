def run():
  #Asking for user input for the direction of travel
  print("Tell me which direction to move (forward, backward, left or right")
  #storing to a variable
  direction = input() 
  #logic to determine response based on direction of travel
  if direction == 'forward':
    print("order received, moving forwards")
  elif direction == 'backward':
    print("roger that, moving backwards")
  elif direction == 'left':
    print("Moving left, no problemo")
  else:
    print("I should probably move right then")
