def likelihood():
  likelihoods = (50, 38, 27, 99, 5)
  return min(likelihoods)

def run():
  print("Minimum likelihood of falling: {}%".format(likelihood()))

run()