#Rewrite your pay computation to give the employee 1.5 times the hourly rate for 
# hours worked aboved 40 hours.
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0
try:
    hours = float(input("plese Enter your Working Hours per week: "))
    rate = float(13)

    if hours > 40:
        pay = hours * (rate * 1.5)
        print("This is your pay per week * 1.5 :", pay)
    else:
        pay = hours * (rate)
        print("This is your pay per week :", pay)
except:
    print('Please Enter your Working Hours in Numbers')