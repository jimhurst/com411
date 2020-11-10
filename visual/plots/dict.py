def data():
  paths = {}

  print("What kind of line would you like to see? (dotted, dashed, solid)")
  line = input()

  print("What kind of colour would you like to see? (red, green, blue")
  colour = input()

  print("What kind of style marker would you like to see? (circle, square, triangle")
  marker = input()

  paths["Line"] = line
  paths["colour"] = colour
  paths["marker"] = marker
  return paths
  
def generate():
  x_data = [2, 4, 6, 8, 10]
  y_data = [2, 2, 2, 2, 2]

  print("How many lines would you like to display?")
  num_lines = int(input())
  for count in range(num_lines):
    plotstyle = data()
    #print(values)
    import matplotlib.pyplot as plt
    plt.plot(x_data, y_data)
    
  plt.show()

def run():
  print("Running...")
  generate()
  print("Done!")

run()



