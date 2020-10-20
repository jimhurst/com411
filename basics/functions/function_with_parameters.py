def run():
  def climb_ladder(steps_rem, steps_cro):
    if steps_rem > steps_cro:
      print("Still some way to go!")
    else:
      print("We are almost there!")

  climb_ladder(5,2)
  climb_ladder(2,5)