def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return (min(likelihoods), max(likelihoods))

def run():
  minans = min(likelihood())
  maxans = max(likelihood())
  print("Minimum likelihood of falling: {}%".format(minans))
  print("Minimum likelihood of falling: {}%".format(maxans))

run()
