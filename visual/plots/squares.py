#import pyplot module
import matplotlib.pyplot as plt

def small():
  xaxis = [3, 4, 4, 3, 3]
  yaxis = [3, 3, 4, 4, 3]
  plt.plot(xaxis, yaxis, 'ro--')
  plt.show()

def medium():
  aaxis = [3, 4, 4, 3, 3]
  baxis = [3, 3, 4, 4, 3]
  caxis = [2, 5, 5, 2, 2]
  daxis = [2, 2, 5, 5, 2]
  plt.plot(aaxis, baxis, caxis, daxis, 'gs--')
  plt.show()

medium()
