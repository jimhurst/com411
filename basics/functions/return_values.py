def run():
  #define the sum weight function
  def sum_weights(weight1, weight2):
    total = weight1 + weight2
    return total

  #define the average weight function
  def calc_avg_weight(weight1, weight2):
    average = (weight1 + weight2) /2
    return average

  #define the run function
  def run():
    print("What is the weight of bot 1?")
    weight1 = float(input())
    print("what is the weight of bot 2?")
    weight2 = float(input())
    print("Would you like to do a sum or average?")
    answer = input()
    if (answer == 'sum'):
      print( sum_weights(weight1, weight2) )
    elif (answer == 'average'):
      print( calc_avg_weight(weight1, weight2) )

  #run
  run()
