def run():
  #define function to render ladder
  def display_ladder(steps):
    for count in range(steps):
      print(" |       | ")
      print(" |       | ")
      print(" +++++++++ ")

  #define function to ask for number of steps and call disply_ladder function
  def create_ladder():
    print("please enter the number of steps")
    steps = int(input())
    display_ladder(steps)

  #call create_ladder function  
  create_ladder()
