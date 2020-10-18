def run():
  def escape_by(route):
    if route == 'jumping over':
      print("We cannot escape that way! The boulder is too big!")
    elif route == 'running around':
      print("We cannot escape that way!")
    elif route == 'going deeper':
      print("That might just work! Let's go deeper!")
    else:
      print("We cannot escape that way! The boulder is in the way!")
  escape_by("jumping over")
  escape_by("running around")
  escape_by("going deeper")