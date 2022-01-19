# Write a program that adds the digits in a 2 digit number. if the inpurt was 35, then the output should be 3 + 5 = 8
# Warning do not change the code on lines 1-3. your program should work for different inputs. ie any two digit number


two_digit_number = input("Type a two digit number in:")

print(type(two_digit_number))

print(two_digit_number)

number_one = two_digit_number[0]
number_two = two_digit_number[1]
sum_of_numbers = int(number_one) + int(number_two)

print(sum_of_numbers)
