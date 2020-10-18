def run():
  #define the cross_bridge function
  def cross_bridge(steps):
    for count in range(steps):
      print("crossed step")
    if steps > 5:
      print("The bridge is collapsing!")
    else:
      print("We must keep going")

  #call the function with a parameter
  cross_bridge(3)
  cross_bridge(6)
