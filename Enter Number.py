# Write a program to accept a number from a user and calculate-
# the sum of all numbers from 1 to a given number For example,
# if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)


print("-------------------- Start Program -----------------------")
number = int(input("plz Enter your Number for Calculate=  "))

for number1 in range(number):
    
    number1 = number + 2
    print("This is your Result ", number1)
print("-------------------- End of Program -----------------------")

