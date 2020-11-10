#import pyplot module
import matplotlib.pyplot as plt

#plots a small red square with dashed lines and circle markers
def small():
  xaxis = [3, 4, 4, 3, 3]
  yaxis = [3, 3, 4, 4, 3]
  plt.plot(xaxis, yaxis, 'ro--')
 
#plots a medium green square with dashed lines and rectangle markers and the small plot above
def medium():
  caxis = [2, 5, 5, 2, 2]
  daxis = [2, 2, 5, 5, 2]
  plt.plot(caxis, daxis, 'gs--')
  
#plots a large blue square with a solid line and pentagon markers as well and the small and medium plots above
def large():
  eaxis = [1, 6, 6, 1, 1]
  faxis = [1, 1, 6, 6, 1]
  plt.plot(eaxis, faxis, 'bp-')
  

small()
medium()
large()
plt.show()
