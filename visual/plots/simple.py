#import pyplot module
import matplotlib.pyplot as plt

#display function to plot a line graph using x and y input
def display(x, y):
  xaxis = x
  yaxis = y
  plt.plot(x, y)
  plt.show()

#run function to call display function passing appropriate x and y data
def run():
  xdata = [1, 2, 3, 4, 5]
  ydata = [1, 4, 9, 16, 25]
  display(xdata, ydata)

run()
