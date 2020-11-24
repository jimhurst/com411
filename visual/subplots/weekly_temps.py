#importing 'pyplot' and 'ticker' and 'csv'
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import csv

def read_data():
  output_dict = {}
  with open("visual/subplots/temps.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = next(csv_reader)
    output_dict[header[0]] = []
    output_dict[header[1]] = []
    for row in csv_reader:
      output_dict[header[0]].append(int(row[0])) 
      output_dict[header[1]].append(int(row[1]))
  return output_dict

def run():
  showme = read_data()
  #print(showme)
  fig, (ax1, ax2) = plt.subplots(1, 2)
  xax = range(len(showme['week1']))
  ax1.plot(xax, showme['week1'])
  ax2.plot(xax, showme['week2'])
  
  plt.tight_layout()
  plt.show()
  

run()