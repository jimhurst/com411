def observed():
  observations = []
  for entry in range(7):
    print("Please enter an observation:")
    entry = input()
    observations.append(entry)
  return observations  

def run():
  observed_output = observed()
  print("Counting observations")
  observed_set = {(observed_output)}
  
  
  #print(observed_output.count("test"))

  

run()
