def short_pattern():
  pattern = {"Sequence":101, "occurences":5}
  return pattern

def medium_pattern():
  pattern = {"Sequence":111000, "occurences":25}
  return pattern

def long_pattern():
  pattern = {"Sequence":1100110011001100, "occurences":50}
  return pattern

def run():
  print("Analysing patterns...")
  short = short_pattern()
  medium = medium_pattern()
  long = long_pattern()
  result = {"short sequence":short, "medium sequence":medium, "long sequence":long}
  for key, value in result.items(): 
    print(f"{key}: {value}")
run()