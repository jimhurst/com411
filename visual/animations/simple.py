import matplotlib.pyplot as plt   
import matplotlib.animation as animation
     
fig, ax = plt.subplots()
    
def animate(frame):    
  plt.xlim(0, 10)
  plt.ylim(0, 10)
  ax[0].plot(frame, frame, 'ro')
  ax[0].set_xlabel('Nice')
  ax[0].set_ylabel('Animation')
     
def run():
  global fig  
  animate = animation.FuncAnimation(fig, animate(), frames = 10, interval = 1000)
  plt.show
      
run()  