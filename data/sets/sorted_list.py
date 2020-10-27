def observed():
  #create a list called observations
  observations = []
  #loop to run 7 times
  for entry in range(5):
    #ask for 7 observations from user and append obervations list
    print("Please enter an observation:")
    entry = input()
    observations.append(entry)
  #return the observations list from this function
  return observations  

def remove_observations(observations):
  is_running = True
  while(is_running):
    print("Do you wish to remove an observation (yes/no)?")
    answer = input()
    if (answer == "yes"):
      print("What observation do you wish to remove?")
      to_remove = input()
      observations.remove(to_remove)
    else:
      is_running = False

def run():
  observations = observed()
  remove_observations(observations)

  observations_set = ()
  for observation in observations:
    occurences = observations.count(observation)
    observations_set.add((observation, occurences))
  
  for key, value in sorted(observations_set):
    print(f"{key} observed {value} times")

run()