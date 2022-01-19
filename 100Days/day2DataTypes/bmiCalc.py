# Write a program that calculates the body mass index from a users weird and height. The BMI is a measure of someones weight taking into account their height.The BMI is calculated by dividing a persons weight, by the square of their height.

height = input("please enter your height")
weight = input('Please enter your weight')

bmi = int(weight) / float(height) ** 2

print(bmi)
