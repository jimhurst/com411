#import pyplot module
import matplotlib.pyplot as plt

def coordinate():
  print("Please enter the value of x")
  xvalue = int.input()
  print("Please enter the value of y")
  yvalue = int.input()
  return (xvalue, yvalue)

coordinate()
