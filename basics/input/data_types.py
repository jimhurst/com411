#Input Questions
print("What is your name?")
name = input()
print("what is your height in metres?")
height = float(input())
print("What is your weight in kilograms ?")
weight = float(input())
print("How old are you in years?")
age = int(input())
#Calculations
bmi = weight / (height ** 2)
#Output
print(f"{name} you are {age} years old and your BMI is {bmi}")