def run():
  #input the variables
  print("please enter the number of lives")
  lives = int(input())
  print("please enter the shield level")
  shield = int(input())
  print("please enter the energy level")
  energy = int(input())
  #render the data
  print("Lives:", "✠" * lives)
  print("Shield:", "❃" * shield)
  print("energy:", "➤" * energy)