import matplotlib.pyplot as plt
import random as rnd

def data():
  paths = {}

  print("What kind of line would you like to see? (-- or : or -)")
  line_style = input()

  print("What kind of colour would you like to see?(r,g,b)")
  colour = input()

  print("What kind of style marker would you like to see? (o,s,^)")
  marker_style = input()

  paths['line_style'] = line_style
  paths['colour'] = colour
  paths['marker_style'] = marker_style

  return paths
  
def generate():
  print("How many lines would you like to display?")
  num_lines = int(input())
  x = [2, 4, 6, 8, 10]
  ycount = 1
  
  for num_line in range(num_lines):
    y = [ycount, ycount, ycount, ycount, ycount]
    values = data()    
    plt.plot(x, y, f"{values['colour']}{values['marker_style']}{values['line_style']}")
    ycount = ycount + 1
  plt.show()

def run():
  print("Running...")
  generate()
  print("Done!")

run()