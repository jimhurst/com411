def observed():
  observations = []
  for entry in range(7):
    print("Please enter an observation:")
    entry = input()
    observations.append(entry)
  return observations  

def run():
  print("Counting observations")
  observed_output = observed()
  observed_set = set()
  for observation in observed_output:
    observed_set.add((observation, observed_output.count(observation)))
  print(observed_set)

  #for step in range(len.observed_output):
  #  observed_set = {(observed_output, observed_output.count)}
  #print(observed_output.count("test"))

  
run()
