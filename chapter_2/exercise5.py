#Write a program which prompts the user for a Celsius temperature , 
#convert the temperature to Fahrenheit, and print out the convert temperature
#°F = °C × (9/5) + 32
celsius = input("Enter celsius temperature: ")
fahrenheit = float(celsius) * (9/5) + 32
print("This is temperature in Fahrenheit: ", fahrenheit)

