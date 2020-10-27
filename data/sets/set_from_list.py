def observed():
  #create a list called observations
  observations = []
  #loop to run 7 times
  for entry in range(7):
    #ask for 7 observations from user and append obervations list
    print("Please enter an observation:")
    entry = input()
    observations.append(entry)
  #return the observations list from this function
  return observations  

def run():
  print("Counting observations")
  #calling the observed function and storing in local variable
  observed_output = observed()
  #creating the observed_output set
  observed_set = set()
  #loop to take each unique value and store it in a tuple along with the count. Stored in the set.
  for observation in observed_output:
    observed_set.add((observation, observed_output.count(observation)))
  #new loop to read out the observation and count from the tuple
  for observation in observed_set:
    print("{} observed {} times.".format(observation[0], observation[1]))
  
  #print(observed_set)
        
run()
