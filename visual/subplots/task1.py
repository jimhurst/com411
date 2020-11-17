#importing pyplot and ticker
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

#defining the read data function
#this function reads from a text file, strips unwanted characters, converts string to int, and then writes each line into a list and returns that
def read_data(file_path):
  output_list = []
  with open (file_path) as textfile:
    for line in textfile:
      line.strip
      output_list.append(int(line))
  return output_list

#defining the run function
#this function calls the read data function and passes the path to the text file. It then creates two subplots arranged horizontally, and then formats each subplot according to the task requirements.
def run():
  result = read_data("visual/subplots/temps.txt")
  fig, axes = plt.subplots(1, 2)
  
  axes[0].plot(range(1,len(result) +1), result)
  axes[0].set_xlabel('Sample')
  axes[0].set_ylabel('Temperature')

  axes[0].tick_params(which='minor', length = 4, color = 'r')
  axes[0].yaxis.set_minor_locator(MultipleLocator(0.5))

  axes[1].bar(range(1,len(result) +1), result)
  axes[1].set_xlabel('Sample')
  axes[1].set_ylabel('Temperature')

  axes[1].tick_params(which='minor', length = 4, color = 'r')
  axes[1].yaxis.set_minor_locator(MultipleLocator(1))

  plt.tight_layout()
  plt.show()
run()



