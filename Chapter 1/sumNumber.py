# Write a program to accept a number from a user and calculate-
# the sum of all numbers from 1 to a given number For example,
# if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)



print("-------------------- Start Program -----------------------")
number = int(input("plz Enter your Number for Calculate=  "))
result = 0
for number1 in range(number):
    result += number1
print("This is your Result ", result)
print("-------------------- End of Program -----------------------")
