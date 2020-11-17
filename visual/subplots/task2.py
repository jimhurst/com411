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

  

showme = read_data()
print(showme)

