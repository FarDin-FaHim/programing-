#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of rane,
#print an error message. If the score is between 0.0 and 1.0. print a grade using the following table
try:
    print('---------- Program to prompt for a Score -----------')
    score = float(input("Enter you Score:>>  "))

    if score >= 0.0 and score <= 1.0:
     if score > 0.9:
        print("your Grade is A")
     elif score > 0.8:
        print('you Grade is B')
     elif score > 0.7:
        print('you Grade is C')
     elif score > 0.6:
         print('you Grade is D')
     elif score < 0.6:
         print('you Grade is E')

    else:
     print("Your score must be between 0.0 and 1.0")

except:
    print("please Entr your Score in Number")




print(""" 
-----------------------
score :     Grade: 
-----------------------
0.9 - 1.0      A
0.8 - 0.89     B
0.7 - 0.79     C
0.6 - 0.69     D
0.0 - 0.59     E
----------------------
 """)

