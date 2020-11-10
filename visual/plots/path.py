def coordinate():
  print("Please enter the value of x")
  xvalue = int(input())
  print("Please enter the value of y")
  yvalue = int(input())
  return (xvalue, yvalue)

def path():
  print("Retrieving path...")
  xvalues = []
  yvalues = []
  for count in range(4):
    data = coordinate()
    xvalues.append(data[0])
    yvalues.append(data[1])
  return [xvalues, yvalues]

def run():
  values = path()
  #print(values)
  import matplotlib.pyplot as plt
  plt.plot(values[0], values[1], 'ro--')
  plt.show()

run()