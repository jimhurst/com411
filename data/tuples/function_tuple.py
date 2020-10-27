def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return (min(likelihoods), max(likelihoods))

def run():
  minans = min(likelihood())
  maxans = max(likelihood())
  print("Minimum likelihood of falling: {}%".format(minans))
  print("Minimum likelihood of falling: {}%".format(maxans))

run()

#def likelihood():
#  likelihoods = (50, 38, 27, 99, 4)
#  return min(likelihoods), max(likelihoods)
#
#def run():
#  probabilities = likelihood()
#  print(f"Minimum likelihood of falling: {probabilities[0]}%")
#  print(f"Maximum likelihood of falling: {probabilities[1]}%")

run()