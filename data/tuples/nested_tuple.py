def steps():
  likelihoods = [("Step 1", 50), ("step 2", 38), ("Step 3", 27), ("Step 4", 99), ("Step 5", 4)]
  return likelihoods

def run():
  all_steps = steps()
  good_steps = []
  bad_steps = []
  for step in all_steps:
    if (step[1] >= 50):
      bad_steps.append(step)
    else:
      good_steps.append(step)
  print("Good Steps: {}, Bad Steps: {}".format(len(good_steps), len(bad_steps)))

run()